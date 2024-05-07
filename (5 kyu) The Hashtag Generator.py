def generate_hashtag(rawtext):
    if rawtext == '':
        return False
    else:
        rawtext = rawtext.split()
        rawtext = [word.capitalize() for word in rawtext]
        gluedtext = ''.join(rawtext)
        hashtag = ('#')
        finaltext = (hashtag + gluedtext)
        if len(finaltext) > 140:
            return False
        else:
            return finaltext
        pass
