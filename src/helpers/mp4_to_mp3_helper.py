
import moviepy.editor

class Mp4toMp3Helper:
    @staticmethod
    def convert(input_file_path, ouput_dir_name):
        playlist_name = ouput_dir_name
        f = input_file_path
        fn = f.split("/")[-1].split(".")[0]
        output = f"./{playlist_name}/mp3/{fn}.mp3"
        v = moviepy.editor.VideoFileClip(f)
        a = v.audio
        a.write_audiofile(output)