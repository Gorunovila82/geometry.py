import requests


__doc__ = "geometry library"
__package__ = "geometry.py"
__version__ = "0.3"

DOWNLOAD_NEW_VERSION = True
PATH = __file__[:-11]

def _download(r):
    res = requests.get(r["zipball_url"]).content
    f = PATH + "v"+r["tag_name"]+".zip"
    open(f,"wb").write(res)
    print(f"Распакуйте обновление {f}!")
    


def _version_check():
    try:
        r = requests.get("https://api.github.com/repos/Gorunovila82/geometry.py/releases").json()[0]
        if __version__ != r["tag_name"]:
            print("Присутствует новая весрсия " + r["tag_name"] + " от "+ r["author"]["login"] + "!") 
            if DOWNLOAD_NEW_VERSION:
                _download(r)

    except:
        pass

_version_check()