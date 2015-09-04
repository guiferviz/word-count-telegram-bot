

import datetime

import telegram


SAMPLE_USER = telegram.User(id=7,
                            first_name='Harry',
                            last_name='Potter',
                            username='sexy_scar')

# User chat, private conversation.
SAMPLE_CHAT = SAMPLE_USER

SAMPLE_DATE = datetime.date(2015, 9, 4)

# TEXT

SAMPLE_TEXT = 'Alohomora'

SAMPLE_TEXT_MESSAGE = telegram.Message(message_id=1,
                                       from_user=SAMPLE_USER,
                                       date=SAMPLE_DATE,
                                       chat=SAMPLE_CHAT,
                                       text=SAMPLE_TEXT)

SAMPLE_TEXT_UPDATE = telegram.Update(update_id=1,
                                     message=SAMPLE_TEXT_MESSAGE)

# STICKER

SAMPLE_STICKER_PHOTOSIZE = telegram.PhotoSize(file_id=0,
                                              width=10,
                                              height=10,
                                              file_size=100)

SAMPLE_STICKER = telegram.Sticker(file_id=0,
                                  width=100,
                                  height=100,
                                  thumb=SAMPLE_STICKER_PHOTOSIZE,
                                  file_size=10000)

SAMPLE_STICKER_MESSAGE = telegram.Message(message_id=1,
                                          from_user=SAMPLE_USER,
                                          date=SAMPLE_DATE,
                                          chat=SAMPLE_CHAT,
                                          sticker=SAMPLE_STICKER)

SAMPLE_STICKER_UPDATE = telegram.Update(update_id=2,
                                        message=SAMPLE_STICKER_MESSAGE)
