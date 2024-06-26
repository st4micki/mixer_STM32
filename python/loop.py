class MixerLoop:
    def __init__(self):
        self.volumes = []
        self.program_on = False
    
    def program_on_set_true(self):
        self.program_on = True
    
    def program_on_set_false(self):
        self.program_on = False
        
    def loop(self, read, audio_obj):
        if self.program_on:
            received_string = read
            if len(received_string) > 23:
                received_string = received_string[2:-5]
                received_split = received_string.split('|')
                self.volumes = []
                for _ in range(len(received_split)):
                    self.volumes.append(float(received_split[_]))
                try:
                    audio_obj.game_volume.SetMasterVolume(self.volumes[0], None)
                except AttributeError:
                    pass
                try:
                    audio_obj.spotify_volume.SetMasterVolume(self.volumes[1], None)
                except AttributeError:
                    pass
                try:
                    audio_obj.chrome_volume.SetMasterVolume(self.volumes[2], None)
                except AttributeError:
                    pass
                try:
                    audio_obj.discord_volume1.SetMasterVolume(self.volumes[3], None)
                    audio_obj.discord_volume2.SetMasterVolume(self.volumes[3], None)
                except AttributeError:
                    pass
            # it should jump to loop function but it will happen in main
        
    