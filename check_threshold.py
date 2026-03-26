# read accuracy
with open("accuracy.txt", "r") as f:
    acc = float(f.read())

print(f"Accuracy = {acc}")

if acc < 0.85:
    raise Exception("Model accuracy is too low! ❌")
else:
    print("Model is good! ✅")
    