import emoji


def remove_emoji(text):
    return emoji.get_emoji_regexp().sub(u'', text)



