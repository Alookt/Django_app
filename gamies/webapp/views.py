from django.shortcuts import render, get_object_or_404
from .models import Book
import PyPDF2
import re

def index(request):
    books = Book.objects.all()
    for book in books:
        print({"title": book.Book_title, "published": book.published})
    return render(request, 'webapp/base.html', {"books": books})

def read(request):
    bookers = Book.objects.all()
    for b in bookers:
        print({"manuscript": b.manuscript})
    return render(request, 'webapp/books.html', {"books": bookers})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    chapters = []
    
    if book.manuscript and book.manuscript.path.endswith('.pdf'):
        try:
            with open(book.manuscript.path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ''
                for page in pdf_reader.pages:
                    text += page.extract_text() + '\n'
                
                # Split into chapters
                chapter_texts = re.split(r'(?=Chapter \d+)', text)
                if len(chapter_texts) > 1:
                    chapters = [{'title': f'Chapter {i+1}', 'content': chapter_texts[i].strip()} for i in range(len(chapter_texts))]
                else:
                    # If no "Chapter" found, split evenly into 10 chapters
                    words = text.split()
                    chapter_size = len(words) // 10 or 1
                    for i in range(0, len(words), chapter_size):
                        chapter_content = ' '.join(words[i:i+chapter_size])
                        chapters.append({'title': f'Chapter {len(chapters)+1}', 'content': chapter_content})
        except Exception as e:
            chapters = [{'title': 'Error', 'content': f'Could not extract text: {str(e)}'}]
    else:
        chapters = [{'title': 'No Manuscript', 'content': 'No PDF manuscript available.'}]
    
    return render(request, 'webapp/book_detail.html', {'book': book, 'chapters': chapters})