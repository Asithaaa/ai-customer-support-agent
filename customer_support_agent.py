import streamlit as st
from openai import OpenAI
import os
import json
from datetime import datetime, timedelta

# Set up the Streamlit App
st.title("AI Customer Support Agent (No Memory) 🛒")
st.caption("Chat with a customer support assistant (memory disabled to avoid Qdrant errors).")

# Set the OpenAI API key
openai_api_key = st.text_input("Enter OpenAI API Key", type="password")

if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key

    class CustomerSupportAIAgent:
        def __init__(self):
            # Memory disabled
            self.memory = None
            self.client = OpenAI()
            self.app_id = "customer-support"

        def handle_query(self, query, user_id=None):
            try:
                # Memory disabled -> no context from past chats
                full_prompt = f"Customer: {query}\nSupport Agent:"

                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a customer support AI agent for TechGadgets.com, "
                                "an online electronics store. Be helpful, clear, and polite."
                            ),
                        },
                        {"role": "user", "content": full_prompt},
                    ],
                )

                answer = response.choices[0].message.content
                return answer

            except Exception as e:
                st.error(f"An error occurred while handling the query: {e}")
                return "Sorry, I encountered an error. Please try again later."

        def get_memories(self, user_id=None):
            # Memory disabled
            return None

        def generate_synthetic_data(self, user_id: str) -> dict | None:
            try:
                today = datetime.now()
                order_date = (today - timedelta(days=10)).strftime("%B %d, %Y")
                expected_delivery = (today + timedelta(days=2)).strftime("%B %d, %Y")

                prompt = f"""Generate a detailed customer profile and order history for a TechGadgets.com customer with ID {user_id}. Include:
1. Customer name and basic info
2. A recent order of a high-end electronic device (placed on {order_date}, to be delivered by {expected_delivery})
3. Order details (product, price, order number)
4. Customer's shipping address
5. 2-3 previous orders from the past year
6. 2-3 customer service interactions related to these orders
7. Any preferences or patterns in their shopping behavior

Format the output as a JSON object."""

                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a data generation AI that creates realistic customer profiles "
                                "and order histories. Always respond with valid JSON."
                            ),
                        },
                        {"role": "user", "content": prompt},
                    ],
                )

                customer_data = json.loads(response.choices[0].message.content)
                return customer_data

            except Exception as e:
                st.error(f"Failed to generate synthetic data: {e}")
                return None

    # Initialize the CustomerSupportAIAgent
    support_agent = CustomerSupportAIAgent()

    # Sidebar for customer ID and profile view
    st.sidebar.title("Enter your Customer ID:")
    previous_customer_id = st.session_state.get("previous_customer_id", None)
    customer_id = st.sidebar.text_input("Enter your Customer ID")

    if customer_id != previous_customer_id:
        st.session_state.messages = []
        st.session_state.previous_customer_id = customer_id
        st.session_state.customer_data = None

    # Button to generate synthetic data
    if st.sidebar.button("Generate Synthetic Data"):
        if customer_id:
            with st.spinner("Generating customer data..."):
                st.session_state.customer_data = support_agent.generate_synthetic_data(customer_id)

            if st.session_state.customer_data:
                st.sidebar.success("Synthetic data generated successfully!")
            else:
                st.sidebar.error("Failed to generate synthetic data.")
        else:
            st.sidebar.error("Please enter a customer ID first.")

    if st.sidebar.button("View Customer Profile"):
        if st.session_state.customer_data:
            st.sidebar.json(st.session_state.customer_data)
        else:
            st.sidebar.info("No customer data generated yet. Click 'Generate Synthetic Data' first.")

    # Initialize the chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    query = st.chat_input("How can I assist you today?")

    if query and customer_id:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        # Generate and display response
        with st.spinner("Generating response..."):
            answer = support_agent.handle_query(query, user_id=customer_id)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.markdown(answer)

    elif not customer_id:
        st.error("Please enter a customer ID to start the chat.")

else:
    st.warning("Please enter your OpenAI API key to use the customer support agent.")
