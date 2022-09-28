import shutil
import click
import sys
import requests as r

def find_installed_player():
    """Find an installed player."""
    # find installed player
    if shutil.which("ffplay"):
        player = ["ffplay", "ffplay", "-nodisp", "-loglevel", "panic"]
    elif shutil.which("cvlc"):
        player = ["cvlc", "cvlc"]
    elif shutil.which("mplayer"):
        player = ["mplayer", "mplayer"]
    else:
        player = None
    return player

def play_url(url):
    """Play an audio streaming url."""
    player = find_installed_player()
    if player is None:
        click.secho("Player NOT found!", fg="red")
        click.secho("Try installing any of the following packages:")
        click.secho("\tffmpeg, vlc or mplayer", bold=True)
        sys.exit(1)
    # launch player
    shutil.os.execlp(*player, url)

def get_link():
    link = r.get('https://virtual-mente.net/radio/').text
    return link

stream_url = get_link()
play_url(stream_url)