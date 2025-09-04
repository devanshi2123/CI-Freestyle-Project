# main.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    result = add(10, 30)
    print(f"Result: {result}")

    # Save result to output.txt
    with open("output.txt", "w") as f:
        f.write(f"Addition result is: {result}\n")
