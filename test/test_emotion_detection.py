import unittest

from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        test_cases = [
            {"text": "I am glad this happened.", "expected_emotion": "joy"},
            {"text": "I am really mad about this.", "expected_emotion": "anger"},
            {"text": "I feel disgusted just hearing about this.", "expected_emotion": "disgust"},
            {"text": "I am so sad about this.", "expected_emotion": "sadness"},
            {"text": "I am really afraid that this will happen.", "expected_emotion": "fear"}
        ]

        for case in test_cases:
            with self.subTest(case=case):
                text = case["text"]
                expected_emotion = case["expected_emotion"]
                result = emotion_detector(text)
                self.assertEqual(result['dominant_emotion'], expected_emotion)

if __name__ == '__main__':
    unittest.main()
