# Thumbnail From Article

## Project Description

This is a python program which takes an article link and generate the summary from each paragraphs. After generating the Paragraph summary it will ask you to select a paragraph. After that it will ask you to press 0 or 1, 0 for searching an article link for images and 1 if you want to give your own image url and after that it will generate the thumbnail for you.

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [Wand](https://docs.wand-py.org/en/0.6.6/)
- [ImageMagick](https://github.com/ImageMagick/ImageMagick)
- [Sumy](https://github.com/miso-belica/sumy)
- [NewsPaper](https://newspaper.readthedocs.io/en/latest/)
- [Requests](https://docs.python-requests.org/en/master/)

## How to get started

1. Clone this repo
2. Inside the folder, you need to create an virtual env. to do that open your terminal/cmd prompt and type the following command one by one.

   ```bash
   python -m venv env
   source env/bin/activate
   ```

3. After creating and activating the virtual env you have to install the requirements. to do that type type the following command in terminal/cmd

   ```bash
   pip install -r requirements.txt
   ```

4. You have to install ImageMagick for image manipulation, to do that visit the offical website of [ImageMagick](https://imagemagick.org/) and download and install it for your os as it support windows, linux and mac.
5. If you are doing NLP (Natural Language Processing) for the first time in Python and have never used the nltk package before you might also have to run the following code in the Python shell:

   ```bash
   import nltk
   nltk.download('punkt')
   ```

6. Now you are good to go, to open the program you just need to type

   ```bash
   python main.py
   ```
