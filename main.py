def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(len(file_contents.split()))

main()