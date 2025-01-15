import unittest
from EmotionDetection.emd_app import emotion_detection
class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        text = "I am so happy I am doing this."
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'joy')

if __name__ == '__main__':
    unittest.main()
