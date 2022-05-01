import unittest
from app.article import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('BBC','Kenya got independence','/khsjha27hbs','/khsjha27hbs','20.02.2022','general',)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
