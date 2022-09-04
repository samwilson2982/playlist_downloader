from pytube import YouTube
import re


class YoutubeManager:

    @staticmethod
    def download_video(url, index, output_folder_name):
        try:
            yt = YouTube(url)
            video_name = YoutubeManager.remove_weird_chars(yt.title.replace(" ", "_"))
            if len(video_name) < 3:
                video_name = url.split("watch?v=")[1].split("&index")[0]
            name = str(index) + "_" + video_name
            print("downloading: ", url, f"'{name}'")

            yt.streams.filter(progressive=True, file_extension="mp4").first().download(
                output_path=f"./{output_folder_name}/mp4/", filename=name + ".mp4"
            )
        except Exception as e:
            print(f"error downloading: {url}, error is: {str(e)}")

    @staticmethod
    def remove_weird_chars(string):
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   u"\U00002500-\U00002BEF"  # chinese char
                                   u"\U00002702-\U000027B0"
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   u"\U0001f926-\U0001f937"
                                   u"\U00010000-\U0010ffff"
                                   u"\u2640-\u2642"
                                   u"\u2600-\u2B55"
                                   u"\u200d"
                                   u"\u23cf"
                                   u"\u23e9"
                                   u"\u231a"
                                   u"\ufe0f"  # dingbats
                                   u"\u3030"
                                   "]+", flags=re.UNICODE)
        string = emoji_pattern.sub(r'', string)
        bad_chars = '<>:"/\\|?*'
        for b in bad_chars:
            string = string.replace(b, "")
        return string
