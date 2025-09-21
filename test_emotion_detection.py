# Import the function to analyze and the unittest library
from EmotionDetection.emotion_detection import emotion_detector
import unittest

# Define the class to test the cases
class TestDominantEmotion(unittest.TestCase):
    def test_dominant_emotion(self):

        # Test case for dominant emotion: joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case for dominant emotion: anger
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test case for dominant emotion: disgust
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test case for dominant emotion: sadness
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Test case for dominant emotion: fear
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')        

# Call the test
unittest.main()