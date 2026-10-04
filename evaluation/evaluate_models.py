"""
Model Evaluation
This script compares a base Qwen model with two fine-tuned cooking models
using the same five Indian cooking questions.

Models:
- Base: qwen2.5:1.5b
- V1: chefmate-cooking:latest
- V2: chefmate-v2:latest

The comparison helps evaluate domain-specific cooking responses after fine-tuning.
"""

import subprocess
import json
from pathlib import Path

QUESTIONS = [
    "How do I prepare dal tadka?",
    "How can I substitute paneer in a vegetarian Indian recipe?",
    "How should I store cooked rice safely?",
    "Why is my roti becoming hard and dry?",
    "How can I make a vegetarian Indian curry less spicy?",
]

MODELS = {
    "Base": "qwen2.5:1.5b",
    "V1": "chefmate-cooking:latest",
    "V2": "chefmate-v2:latest",
}

def ask_model(model_name, question):
    """Send one question to an Ollama model and return its response."""

    result = subprocess.run(
        ["ollama", "run", model_name, question],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    if result.returncode != 0:
        return f"ERROR: {result.stderr.strip()}"

    return result.stdout.strip()

def evaluate_models():
    """Run all questions against Base, V1 and V2 models."""

    results = []

    print("Starting model evaluation...\n")

    for question_number, question in enumerate(QUESTIONS, start=1):

        print("=" * 70)
        print(f"Question {question_number}: {question}")
        print("=" * 70)

        for version, model_name in MODELS.items():

            print(f"\n[{version}] {model_name}")

            response = ask_model(model_name, question)

            print(response)

            results.append(
                {
                    "question_number": question_number,
                    "question": question,
                    "model_version": version,
                    "model_name": model_name,
                    "response": response,
                }
            )

    output_file = Path("evaluation_results.json")

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=2, ensure_ascii=False)

    print("\n" + "=" * 70)
    print("Evaluation completed successfully!")
    print(f"Results saved to: {output_file}")
    print(f"Total evaluations: {len(results)}")
    print("=" * 70)

if __name__ == "__main__":
    evaluate_models()
