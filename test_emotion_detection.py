from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_glad_statement(self):
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_mad_statement(self):
        statement = "I am really mad about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgusted_statement(self):
        statement = "I feel disgusted just hearing about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sad_statement(self):
        statement = "I am so sad about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_afraid_statement(self):
        statement = "I am really afraid that this will happen"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()