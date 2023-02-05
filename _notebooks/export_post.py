import os
from datetime import datetime
import argparse

if __name__ == '__main__':
    # Parse the title of the post from the command line
    parser = argparse.ArgumentParser(description='Export Jupyter notebook to markdown file')
    parser.add_argument('--title', type=str, help='Title of the post')
    parser.add_argument('--target-file', type=str, help='Target file')
    args = parser.parse_args()

    current_date = datetime.now().strftime('%Y-%m-%d')
    title = args.title
    target_file = args.target_file
    out_file = f'../_posts/{current_date}-{title}.md'
    os.system(f'jupyter nbconvert --to markdown {target_file} --output {out_file}')

    print(f'Exported to {out_file}')