import random

# simulate training
accuracy = random.uniform(0.85, 0.95)

print(f"Model accuracy: {accuracy}")

# save accuracy to file (simulate MLflow)
with open("accuracy.txt", "w") as f:
    f.write(str(accuracy))

# simulate run ID
with open("run_id.txt", "w") as f:
    f.write("12345")
    