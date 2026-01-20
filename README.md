
# AI Customer Support Agent 🛒 (Streamlit + OpenAI)

A simple AI-powered customer support chatbot built using **Streamlit** and the **OpenAI API**.  
It simulates customer support for an e-commerce electronics store (**TechGadgets.com**) with a clean chat UI and customer ID based sessions.

> ✅ Note: The original version supports memory using a vector database.  
> In this version, **memory is disabled** to avoid local database setup issues and keep it easy to run.

---

# 🚀 Features
- Interactive **Streamlit Chat UI**
- Customer ID based chat session
- Generates synthetic customer profile + order history (JSON)
- Uses OpenAI for customer support responses
- Beginner-friendly setup

---

# 🛠 Tech Stack
- **Python 3.12**
- **Streamlit**
- **OpenAI Python SDK**

---

# 📦 Setup & Run Locally

### 1) Clone this repository
```bash
git clone https://github.com/Snehaahaa/ai-customer-support-agent.git
cd ai-customer-support-agent
````

### 2) Install dependencies

```bash
py -3.12 -m pip install streamlit openai
```

### 3) Run the app

```bash
py -3.12 -m streamlit run customer_support_agent.py
```

After running, open the browser link shown in terminal (usually):

* [http://localhost:8501](http://localhost:8501)

---

## 🔑 OpenAI API Key

When the app opens, enter your **OpenAI API key** in the input field.

⚠️ Never share your API key publicly.

---

## 📌 How to Use

1. Enter your OpenAI API key
2. Enter a Customer ID (example: `cust101`)
3. Start chatting in the chat box
4. (Optional) Click **Generate Synthetic Data** to create a sample customer profile

---

## 🙌 Credits / Attribution

This project is based on and inspired by the **awesome-llm-apps** repository by **Shubhamsaboo**.

Source repository:
[https://github.com/Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

---

## 📄 License

The original source project (**awesome-llm-apps**) is licensed under the **Apache License 2.0**.
This repository contains modifications for learning and local execution.

You can view the original license here:
[https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/LICENSE](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/LICENSE)

---

## 👩‍💻 Author

**Sneha G**

```


