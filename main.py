def add(a, b):
    return a + b

if __name__ == "__main__":
    result = add(2, 3)
    with open("output.txt", "w") as f:
        f.write(f"Result: {result}\n")
    print(f"Result: {result}")
