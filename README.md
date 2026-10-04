# GROWAI LLM Engineering - Assignment 10

## Fine-Tune & Deploy a Domain-Specific LLM

This project demonstrates the fine-tuning and local deployment of a **domain-specific Indian cooking assistant** called **ChefMate** using **Qwen2.5-1.5B-Instruct**.

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

Fine-tuning was performed in **Google Colab using a GPU and Unsloth**. The complete training notebook is included in:

```text
training/ChefMate_FineTuning.ipynb
```

### 2. Dataset

The final cooking dataset contains **76 validated examples** covering:

* Indian recipes
* Ingredient substitutions
* Cooking techniques
* Food storage
* Vegetarian and vegan cooking
* Cooking troubleshooting

The ChatML training dataset is available at:

```text
dataset/chatml_cooking_dataset_v2.json
```

Dataset validation is performed using:

```text
dataset/validate_chatml_v2.py
```

The validation completed successfully with **76 total examples and 0 validation errors**.

### 3. Ollama Deployment

The fine-tuned model was exported as a **GGUF Q4_K_M** model.

The GGUF model and Modelfile are available in:

```text
deployment/
```

Using the provided `Modelfile`, create the local Ollama model:

```text
ollama create chefmate -f Modelfile
```

Run the model:

```text
ollama run chefmate
```

The deployed model was tested successfully with Indian cooking questions.

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
| Trainable Parameters  | 1.18%                 |
| Output Format         | GGUF Q4_K_M           |

Training loss decreased during the 100-step training process, indicating that the model learned from the cooking-domain training data.

## Model Evaluation & Comparison

The **base model, V1 fine-tuned model and V2 fine-tuned model** were evaluated using the same five cooking questions.

The evaluated models were:

| Version | Ollama Model              |
| ------- | ------------------------- |
| Base    | `qwen2.5:1.5b`            |
| V1      | `chefmate-cooking:latest` |
| V2      | `chefmate-v2:latest`      |

The five evaluation questions were:

1. How do I prepare dal tadka?
2. How can I substitute paneer in a vegetarian Indian recipe?
3. How should I store cooked rice safely?
4. Why is my roti becoming hard and dry?
5. How can I make a vegetarian Indian curry less spicy?

This resulted in **15 total model evaluations**.

The complete evaluation output is saved in:

```text
evaluation/evaluation_results.json
```

The evaluation showed that the fine-tuned models generally produced more cooking-focused responses than the base model. However, some responses still contained factual or food-safety limitations. This demonstrates that fine-tuning improves domain behavior but does not guarantee complete factual accuracy.

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

Fine-tuning on a relatively small dataset does not guarantee factual accuracy.

The dataset validation script checks for:

* Missing `messages` fields
* Incorrect number of messages
* Incorrect message roles
* Empty user messages
* Empty assistant messages

The final dataset passed validation with **0 errors**.

During model evaluation, some generated responses also contained questionable cooking procedures or food-safety guidance. This shows the importance of manual review and additional grounding for safety-sensitive cooking information.

## Project Files

```text
FineTune_Domain_Specific_LLM/
│
├── dataset/
│   ├── chatml_cooking_dataset_v2.json
│   ├── final_cooking_dataset_v2_clean.json
│   └── validate_chatml_v2.py
│
├── deployment/
│   ├── Modelfile
│   └── Qwen2.5-1.5B-Instruct.Q4_K_M.gguf
│
├── evaluation/
│   ├── evaluate_models.py
│   └── evaluation_results.json
│
├── training/
│   └── ChefMate_FineTuning.ipynb
│
├── requirements.txt
├── .gitignore
└── README.md
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
