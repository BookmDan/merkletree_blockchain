# Script to generate test files
def create_test_files():
    files_content = {
        "file1.txt": "Content of file1.txt",
        "file2.txt": "Content of file2.txt",
        "file3.txt": "Content of file3.txt"
    }

    for filename, content in files_content.items():
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Created {filename}")

# Run the script to create the files
if __name__ == "__main__":
    create_test_files()
