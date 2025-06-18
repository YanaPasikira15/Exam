from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def print(self):
        pass
    
    def prepare_for_printing(self):
        print("Preparing document for printing...")
        self.print()
        print("Document ready!")


class PDFDocument(Document):
    def print(self):
        print("Printing PDF document with special formatting")


class WordDocument(Document):
    def print(self):
        print("Printing Word document with headers and footers")


class ExcelDocument(Document):
    def print(self):
        print("Printing Excel document with grid lines")


class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == "pdf":
            return PDFDocument()
        elif doc_type == "word":
            return WordDocument()
        elif doc_type == "excel":
            return ExcelDocument()
        else:
            raise ValueError(f"Unknown document type: {doc_type}")


# Приклад використання
if __name__ == "__main__":
    documents = [
        DocumentFactory.create_document("pdf"),
        DocumentFactory.create_document("word"),
        DocumentFactory.create_document("excel")
    ]
    
    for doc in documents:
        print(f"\nProcessing {doc.__class__.__name__}:")
        doc.prepare_for_printing()
