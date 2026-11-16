import unittest
from unittest.mock import patch
from langchain_ollama import ChatOllama
from src.agent.graph import build_graph
from src.retrieval.retriever import retrieve_text
import tempfile
from pathlib import Path

class TestAgentRetrieval(unittest.TestCase):

    def test_retrieved_context_reaches_model(self):
        question = "Which tool stores vectors and finds similar information?"
        retrieved_text = retrieve_text(question)
        self.assertIn("Qdrant", retrieved_text)

        original_invoke = ChatOllama.invoke

        with patch.object(ChatOllama, "invoke", autospec=True, side_effect=original_invoke) as spy:
            graph = build_graph()
            result = graph.invoke({
                "question": question,
                "use_retrieval": True,
                "model_name": "llama3.2:latest"
            })

            spy.assert_called_once()
            args, _ = spy.call_args
            
            model_instance = args[0]
            prompt = args[1]

            self.assertEqual(model_instance.model, "llama3.2:latest")
            self.assertIn(question, prompt)
            self.assertIn(retrieved_text, prompt)

            answer = result.get("answer")
            self.assertIsInstance(answer, str)
            self.assertTrue(len(answer) > 0)
    def test_empty_document_reports_retrieval_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = Path(temp_dir) / "empty.txt"
            temp_file.write_text("   \n   ")

            with patch.object(ChatOllama, "invoke", autospec=True) as spy:
                graph = build_graph()
                with self.assertRaises(ValueError) as ctx:
                    graph.invoke({
                        "question": "What is this?",
                        "use_retrieval": True,
                        "model_name": "llama3.2:latest",
                        "document_path": str(temp_file)
                    })

                self.assertIn("No text was retrieved from the document", str(ctx.exception))
                spy.assert_not_called()

if __name__ == "__main__":
    unittest.main()