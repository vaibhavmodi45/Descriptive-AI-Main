# app.py
from flask import Flask, request, jsonify
from transformers import pipeline, GPT2LMHeadModel, GPT2Tokenizer

# Load the fine-tuned model and tokenizer
try:
    model = GPT2LMHeadModel.from_pretrained('./fine_tuned_model')
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
except Exception as e:
    print(f"Error loading model: {e}")
    generator = None

def generate_description(input_text):
    if generator is None:
        return "Model not available"
    # Generate description with a length of 3 to 5 lines
    prompt = f"Generate a detailed description for: {input_text}"
    result = generator(prompt, max_length=150, min_length=50, num_return_sequences=1)
    generated_text = result[0]['generated_text']
    # Remove the prompt from the generated text
    description = generated_text.replace(prompt, "").strip()
    return description

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    input_text = data.get('input_text', '')
    if not input_text:
        return jsonify({'error': 'No input text provided'}), 400
    description = generate_description(input_text)
    return jsonify({'description': description})

if __name__ == '__main__':
    app.run(debug=True)