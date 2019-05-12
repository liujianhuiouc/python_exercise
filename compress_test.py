
import zlib
import base64


def decompress_data(d):
    """decompress data
    """
    if not isinstance(d, (str, unicode)):
        return d
    decode_data = base64.b64decode(str(d))
    r = zlib.decompress(decode_data)
    return r


if __name__ == '__main__':
    print(decompress_data('eJxVUcuOwjAM/JWVzxVK36U3vmOLIrekS7ShVElcgVD/fV0aynJJHHucmbEfQE7JDruzgrpH41QE3Rmth/oBTlmtHNTfD/ixVxple5f+PjISIAI1qcFLg60ynDhsmQEvCwLHkYs0dOePikSj0a31hvIs6flMsGKQdvKkHbZGnaAeyJgIrHJk/JNU0qD9yozeWzmhIfUi4+RoVa9v8lfdA2j6gbrYiQhO6JFNlBwv73wnjp8/vzw0VIi0bajMk4rjJC35zEvRUN+Liqbnvee/A+sh+or5tc1m5ZZs0WyeNXvZp1kcgePuTeAL5OgCdVwtMnttvAq+nmLyuGAZWZ+n/yWtg+qul5H8e2ehOTiJP/wtqwxrWzXxyq2DeeYx3A437RZAGBIkIt6LTBRME8LyHVZwnOf5DwUStJk='))
