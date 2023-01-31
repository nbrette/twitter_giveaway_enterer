import emoji


def remove_emoji(text):

    found_emojis = emoji.emoji_list(text)
    found_emojis.reverse()
    for found_emoji in found_emojis:
        text = text[:found_emoji['match_start']] + text[found_emoji['match_start'] + 1:]
    return text
        



