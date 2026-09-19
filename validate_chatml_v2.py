import json

INPUT_FILE = "chatml_cooking_dataset_v2.json"

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    dataset = json.load(file)

errors = []

for index, example in enumerate(dataset, start=1):

    if "messages" not in example:
        errors.append(f"Example {index}: missing messages")
        continue

    messages = example["messages"]

    if len(messages) != 2:
        errors.append(
            f"Example {index}: expected 2 messages, found {len(messages)}"
        )
        continue

    if messages[0].get("role") != "user":
        errors.append(f"Example {index}: first role is not user")

    if messages[1].get("role") != "assistant":
        errors.append(f"Example {index}: second role is not assistant")

    if not messages[0].get("content", "").strip():
        errors.append(f"Example {index}: empty user content")

    if not messages[1].get("content", "").strip():
        errors.append(f"Example {index}: empty assistant content")

print("ChatML validation started...\n")
print("Total examples:", len(dataset))
print("Validation errors:", len(errors))

if errors:
    print("\nProblems found:")
    for error in errors:
        print("-", error)
else:
    print("\n All ChatML examples are valid!")
    print("Every example has user + assistant messages")
    print("No empty messages")
    print("Correct message roles")

print("\nChatML validation completed.")