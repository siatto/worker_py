from utils import count_words_at_url

result = q.enqueue(count_words_at_url, 'http://heroku.com')
