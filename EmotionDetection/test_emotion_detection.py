from emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    
    def test_emotion_detector_success(self):
        text = "I am glad this happened."
        result = emotion_detector(text)
        
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_emotion_detector_success(self):
        text = "I am really mad about this"
        result = emotion_detector(text)
        
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_detector_success(self):
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_emotion_detector_success(self):
        text = "I am so sad about this"
        result = emotion_detector(text)
        
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_emotion_detector_success(self):
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
