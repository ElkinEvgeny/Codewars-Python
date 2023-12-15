def generate_hashtag(s):
    s = s.title().replace(" ", "")
    return s.rjust(len(s)+1, "#") if 140 > len(s) > 1 else False
