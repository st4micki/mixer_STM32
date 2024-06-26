from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume


class Audio:
    def __init__(self):
        self.spotify_volume = None
        self.chrome_volume = None
        self.discord_volume1 = None
        self.discord_volume2 = None
        self.game_volume = None
        self.sessions = []
        self.process_names = []
        self.sessions = None
        self.devices = None
        self.interface = None
        self.chosen_game = None
        self.session_skip = 0

    def get_sessions(self):
        self.devices = AudioUtilities.GetSpeakers()
        self.interface = self.devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.sessions = AudioUtilities.GetAllSessions()
        self.process_names = []
        for session in self.sessions:
            print(session)
            if session.Process:
                self.process_names.append(session.Process.name())

    def audio_setup(self, game):
        self.session_skip = 0
        for session in self.sessions:
            if session.Process and session.Process.name() == game:
                self.game_volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            elif session.Process and session.Process.name() == "Spotify.exe":
                self.spotify_volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            elif session.Process and session.Process.name() == 'chrome.exe':
                self.chrome_volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            elif session.Process and session.Process.name() == 'Discord.exe':
                if self.session_skip < 1:
                    self.discord_volume1 = session._ctl.QueryInterface(ISimpleAudioVolume)
                else:
                    self.discord_volume2 = session._ctl.QueryInterface(ISimpleAudioVolume)
                self.session_skip += 1

        #it should jump to loop function but it will happen in main
        #in main program_on flag should be changed after this method

