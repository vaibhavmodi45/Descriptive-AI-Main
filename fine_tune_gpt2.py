import pandas as pd
from datasets import Dataset
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling

def load_and_prepare_dataset(csv_path):
    df = pd.read_csv(csv_path)
    
    df['text'] = df['Input'] + " " + df['Output']
    
    dataset = Dataset.from_pandas(df[['text']])
    return dataset

def main():
    model_name = 'gpt2'
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    tokenizer.pad_token = tokenizer.eos_token
    
    model = GPT2LMHeadModel.from_pretrained(model_name)

    dataset = load_and_prepare_dataset('50dataset.csv')

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
