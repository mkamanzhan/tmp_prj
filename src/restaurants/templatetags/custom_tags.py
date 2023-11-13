from django import template

register = template.Library()

censored_words = ["fuck", "asshole", "pidaras"]


@register.simple_tag
def censor(value):
    """
    Replace bad word from censored_words in text to stars
    """
    result = []
    words = value.split()
    for word in words:
        has_bad_words = False
        for censored_word in censored_words:
            if censored_word.lower() in word.lower():
                has_bad_words = True
                break
        if has_bad_words:
            result.append("***")
        else:
            result.append(word)
    return " ".join(result)
