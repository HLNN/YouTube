from download import Download

import os
import re


class Youtube:
    def __init__(self):
        self.workingPath = ""

    def main(self):
        taskfile = input("Please input your task list file name:") or "./taskfile.txt"
        with open(taskfile, "r", encoding='UTF-8') as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            if re.match("\d{1,2}. ", line):
                if not os.path.exists(line):
                    os.mkdir(line)
                if self.workingPath:
                    os.system("mv *.mp4 '{lastpath}'/".format(lastpath=self.workingPath))
                self.workingPath = line
                print(line)
            elif re.findall("https://www.youtube.com/watch\?v=", line):
                video_id = re.findall("https://www.youtube.com/watch\?v=(.*)", line)[0]
                youtube = Download(video_id, self.workingPath)
                youtube.main()
        os.system("mv *.mp4 '{lastpath}'/".format(lastpath=self.workingPath))
        os.system("zip -r cupt.zip ./*")


if __name__ == '__main__':
    youtube = Youtube()
    youtube.main()
