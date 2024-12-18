# fine_tune_gpt2.py
import pandas as pd
from datasets import Dataset
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling

def load_and_prepare_dataset(csv_path):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_path)
    
    # Combine the 'Input' and 'Output' columns to create the training text
    df['text'] = df['Input'] + " " + df['Output']
    
    # Convert the DataFrame to a Hugging Face Dataset
    dataset = Dataset.from_pandas(df[['text']])
    return dataset

def main():
    model_name = 'gpt2'
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    
    # Set the padding token
    tokenizer.pad_token = tokenizer.eos_token
    
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Load and prepare the dataset
    dataset = load_and_prepare_dataset('50dataset.csv')
    
    # Tokenize the dataset
    def tokenize_function(examples):
        return tokenizer(examples['text'], truncation=True, padding='max_length', max_length=128)
    
    tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=['text'])

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,
    )

    training_args = TrainingArguments(
        output_dir='./results',
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=10_000,
        save_total_limit=2,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=tokenized_dataset,
    )

    trainer.train()
    trainer.save_model('./fine_tuned_model')

if __name__ == "__main__":
    main()