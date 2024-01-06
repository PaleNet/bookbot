def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    count = word_count(text)
    print(count)
    
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    
def word_count(text):
    words = get_book_text(text).split()
    return words.count()