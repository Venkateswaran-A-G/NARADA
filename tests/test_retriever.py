import unittest
import tempfile
from pathlib import Path
from src.retrieval.retriever import retrieve_text


class TestRetriever(unittest.TestCase):

    def test_search_sample_question(self):
        """Test searching for the known fact in the sample document."""
        question = "Which tool stores vectors and finds similar information?"
        result = retrieve_text(question)
        self.assertEqual(result, "Qdrant stores vectors and finds similar information.")

    def test_blank_document_handling(self):
        """Test passing a temporary document with only whitespace lines."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = Path(temp_dir) / "blank.txt"
            temp_file.write_text("   \n\t\n   ")
            
            result = retrieve_text("Some question", document_path=temp_file)
            self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()