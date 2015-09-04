

import json
from webtest import app
from mock import patch

import test_suite
import telegram_token

import utils


BOT_URL = '/' + telegram_token.TOKEN


class HandlersTests(test_suite.AppEngineTestBase):

    def test_404_when_root_post_request(self):
        """
        Checks telegram bot webhook is not the root path.
        """
        try:
            self.testapp.post('/')
            raise Exception('No 404 error asking for "/"')
        except app.AppError as error:
            self.assertTrue('404 Not Found' in error.message)

    def test_empty_body_request(self):
        """
        Request with empty JSON body.
        """
        self.testapp.post(BOT_URL)

    def test_garbage_request(self):
        """
        Not empty and invalid JSON body.
        """
        self.testapp.post(BOT_URL, 'garbage')

    def test_json_garbage_request(self):
        """
        Request with valid JSON body but not as expected.
        """
        self.testapp.post(BOT_URL, '{}')

    @patch('telegram.Bot.sendMessage')
    def test_text_message(self, mock_send_message):
        """
        Checks that the bot does an echo with all the text messages it receives.
        """
        json_str_body = json.dumps(utils.SAMPLE_TEXT_UPDATE.to_dict())
        self.testapp.post(BOT_URL, json_str_body)
        mock_send_message.assert_called_once_with(chat_id=utils.SAMPLE_CHAT.id,
                                                  text=utils.SAMPLE_TEXT)

    @patch('telegram.Bot.sendMessage')
    def test_sticker_message(self, mock_send_message):
        """
        Checks that the bot doesn't respond to stickers.
        """
        json_str_body = json.dumps(utils.SAMPLE_STICKER_UPDATE.to_dict())
        self.testapp.post(BOT_URL, json_str_body)
        self.assertFalse(mock_send_message.called)
