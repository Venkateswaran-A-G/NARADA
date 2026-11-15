import unittest
from unittest.mock import patch
from langchain_ollama import ChatOllama
from src.agent.graph import build_graph


class TestModelSelection(unittest.TestCase):

    def test_selected_model(self):
        with patch("src.agent.model_factory.ChatOllama", wraps=ChatOllama) as spy:
            graph = build_graph()
            
            result = graph.invoke({
                "question": "What is the capital of France?",
                "model_name": "llama3.2:latest"
            })

            answer = result.get("answer")
            self.assertIsInstance(answer, str)
            self.assertTrue(len(answer) > 0)

            self.assertEqual(result.get("model_name"), "llama3.2:latest")

            spy.assert_called_once()
            _, kwargs = spy.call_args
            self.assertEqual(kwargs.get("model"), "llama3.2:latest")
            self.assertEqual(kwargs.get("temperature"), 0)

            
    def test_default_model(self):
        with patch("src.agent.model_factory.ChatOllama", wraps=ChatOllama) as spy:
            graph = build_graph()
            
            result = graph.invoke({
                "question": "What is the capital of France?"
            })

            answer = result.get("answer")
            self.assertIsInstance(answer, str)
            self.assertTrue(len(answer) > 0)

            self.assertEqual(result.get("model_name"), "llama3.2:latest")

            spy.assert_called_once()
            _, kwargs = spy.call_args
            self.assertEqual(kwargs.get("model"), "llama3.2:latest")


if __name__ == "__main__":
    unittest.main()