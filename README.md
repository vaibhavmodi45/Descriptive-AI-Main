# Descriptive AI

**Description:**
Descriptive AI is a web application designed to generate detailed descriptions based on userprovided input. It leverages the GPT-2 model from Hugging Face Transformers for text generation. The application is built using Flask for the backend and Streamlit for the frontend. This document provides an overview of the project, including its objectives, design, implementation, and results.

<br>

**Objectives:**

❑ To create a user-friendly web application for 
generating descriptions.

❑ To fine-tune the GPT-2 model on a custom 
dataset for improved performance.

❑ To integrate the backend and frontend 
seamlessly for optimal user experience.

<br>


****Architecture:****
The application consists of three main components:
<br>
<br>
• **Fine-Tuning Script:** Prepares the dataset, tokenizes it, and finetunes the GPT-2 model.

**• Flask Backend:** Loads the fine-tuned model and handles requests to generate descriptions.

**• Streamlit Frontend:** Provides a user interface for input and displays the generated descriptions


<br>
<br>

**Getting Started:**

Step 1. **Enter Title:**
![1](https://github.com/user-attachments/assets/cee0cc71-beb7-4b10-9011-30da11740ed7)
   - Open the application or access the tool.
   - Locate the input field for the title.
   - Enter the desired title for your project or content.

<br>

Step 2. **Click on the Generate button.**
![2](https://github.com/user-attachments/assets/6a09da5b-3f06-4478-a25c-6a7612f19923)
   - Click on the "Generate" button to initiate the content generation process.

<br>

Step 3. **Get your Generated Description:**
![3](https://github.com/user-attachments/assets/1ea29e51-e92c-4121-9537-7c0d78454d12)
   - The generated description will be displayed in the designated area below the "Generated Content for:" label.
