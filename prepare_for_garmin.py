#convert gpx tracks with russian symbols to tracks with translit symbols to use in in best garmin apps
import cyrtranslit
import sys
import argparse
import os

def process_file(f, src, dest, lang):
    ext = os.path.splitext(f)[-1]
    translated = cyrtranslit.to_latin(f, lang).replace('\'', '')
    print(ext, f, '--', translated, '/', lang)

    fout = open(os.path.join(dest, translated), "w")
    with open(os.path.join(src, f), "r") as fin:
        for line in fin:
            fout.write(cyrtranslit.to_latin(line, lang))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Converts gpx files to use with garmin software')
    parser.add_argument('src_path', type=str, help='path to gpx files')
    parser.add_argument('out_path', type=str, help='output path to gpx files')
    parser.add_argument('--lang', type=str, help='gpx files language', default='ru')
    args = parser.parse_args()

    os.makedirs(args.out_path, exist_ok=True)

    file_list = [f for f in os.listdir(args.src_path) if os.path.isfile(os.path.join(args.src_path, f))] 
    file_list = list(filter(lambda x : os.path.splitext(x)[-1] == '.gpx', file_list))

    [process_file(f, args.src_path, args.out_path, args.lang) for f in file_list]



