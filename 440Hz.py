# Nefunguje, kvůli tomu, že v NB není nainstalován doplněk FFMPEG 

from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play

# Vytvoření zvukového souboru
duration = 3000  # Doba trvání zvuku v milisekundách
frequency = 440  # Frekvence zvuku v Hz

# Generování tónu
sine_wave = Sine(frequency).to_audio_segment(duration=duration)

# Přehrání zvuku
play(sine_wave)
