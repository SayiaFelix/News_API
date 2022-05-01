import unittest
from app.news import Source,TopHeadlines

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('BBC','Kenya got independence','/khsjha27hbs','general','uk')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


class TopHeadlinesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the TopHeadlines classs
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_TopHeadlines = ('SirFelix','BBC','Kenya got independence','/khsjha27hbs','general kenya','/khsjha27hbs','20.05.2021')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_TopHeadlines,TopHeadlines))