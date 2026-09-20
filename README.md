# GROWAI LLM Engineering - Assignment 10

## Fine-Tune & Deploy a Domain-Specific LLM

This project demonstrates the fine-tuning and local deployment of a **domain-specific cooking assistant** using **Qwen2.5-1.5B-Instruct**.

A custom dataset of **76 cooking-related instruction-response examples** was validated, formatted in ChatML and used for parameter-efficient fine-tuning with **LoRA/QLoRA and Unsloth**. The fine-tuned model was exported to **GGUF Q4_K_M** format and deployed locally using **Ollama**.

## Features

* Custom cooking-domain dataset creation and validation
* ChatML dataset formatting
* LoRA/QLoRA fine-tuning
* 4-bit quantized training
* GGUF Q4_K_M model export
* Local Ollama deployment
* Base model vs V1 vs V2 evaluation
* Cooking-domain instruction following
* Edge-case and response-quality evaluation

## Technologies Used

* Python
* Qwen2.5-1.5B-Instruct
* Unsloth
* PyTorch
* Hugging Face Transformers
* Hugging Face Datasets
* TRL
* PEFT
* Ollama
* GGUF

## Requirements

* Python 3.x
* Google Colab with GPU for fine-tuning
* Ollama for local inference
* Dependencies listed in `requirements.txt`

## Setup / Installation

### 1. Install Dependencies

```text
pip install -r requirements.txt
```

Fine-tuning was performed in Google Colab using a GPU and Unsloth.

### 2. Dataset

The final dataset contains **76 validated cooking-related examples** covering:

* Indian recipes
* Ingredient substitutions
* Cooking techniques
* Ingredient-based meals
* Food storage
* Vegetarian and vegan cooking
* Cooking troubleshooting

The ChatML training dataset is available at:
```text
dataset/chatml_cooking_dataset_v2.json
```

### 3. Ollama Deployment

The fine-tuned model was exported as a GGUF Q4_K_M model.

Using the provided `Modelfile`, create the local Ollama model:
```text
ollama create chefmate-v2 -f Modelfile
```

Run the model:
```text
ollama run chefmate-v2
```

## Fine-Tuning Configuration

| Parameter             | Value                 |
| --------------------- | --------------------- |
| Base Model            | Qwen2.5-1.5B-Instruct |
| Dataset               | 76 examples           |
| Method                | LoRA / QLoRA          |
| LoRA Rank             | 16                    |
| Training Steps        | 100                   |
| Learning Rate         | 2e-4                  |
| Training Quantization | 4-bit                 |
| Output Format         | GGUF Q4_K_M           |

## Model Evaluation & Comparison

The **base model, original fine-tuned model (V1) and improved fine-tuned model (V2)** were evaluated using the same five cooking questions:

1. Dal tadka preparation
2. Paneer substitution
3. Fixing an overly salty curry
4. Safe cooked-rice storage
5. Vegetarian meal using potatoes and spinach

V2 showed improved cooking-domain alignment and better adherence to user-provided ingredients in several test cases. However, the evaluation also identified remaining recipe and food-safety limitations.

For example, V2 correctly generated a vegetarian potato-spinach curry, while V1 introduced meat-based sausage despite the vegetarian requirement.

## Fine-Tuning vs RAG vs Prompt Engineering

| Approach           | Model Weights | External Knowledge | Training | Primary Use                             |
| ------------------ | ------------- | ------------------ | -------- | --------------------------------------- |
| Prompt Engineering | No            | Optional           | No       | Behavior and output control             |
| RAG                | No            | Yes                | No       | Dynamic, knowledge-grounded information |
| Fine-Tuning        | Yes           | Not required       | Yes      | Domain-specific behavior                |

For a production version of ChefMate, these approaches can be combined:

**Fine-Tuning + RAG + Prompt Engineering**

Fine-tuning can provide specialized cooking behavior, RAG can supply validated and updateable knowledge and prompt engineering can control response format and interaction.

## Real-World Relevance

ChefMate can serve as a foundation for:

* Recipe assistants
* Ingredient-based meal recommendations
* Cooking troubleshooting
* Ingredient substitution
* Food-storage guidance
* Voice-based cooking assistance

## Edge Case / Failure Point

Fine-tuning on a relatively small dataset does not guarantee factual accuracy. During evaluation, some responses contained questionable cooking procedures and food-safety guidance.

Dataset validation, duplicate removal and manual review can reduce these issues, while a trusted RAG knowledge base can provide additional grounding for safety-critical information.

## Project Files

```text
dataset/
├── chatml_cooking_dataset_v2.json
├── final_cooking_dataset_v2_clean.json
└── validate_chatml__v2.py

deployment/
└── Modelfile

requirements.txt
.gitignore
```

## Future Improvements

* Expand and manually validate the training dataset
* Integrate a trusted RAG knowledge base
* Add Hindi and Hinglish support
* Improve food-safety knowledge
* Expand evaluation with more test cases
* Add voice-based cooking interaction
* Integrate personalized recipe recommendations
* Explore production inference and quantization optimization

## Assignment

GROWAI LLM Engineering & Generative AI - Assignment 10
