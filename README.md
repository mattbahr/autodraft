I wrote this command line tool to save time sending booking inquiries for my band. This has been tested with Python 3.6.
The program uses template files to generate text customized with user input. It then copies the text to the clipboard
so that it can be pasted into a text editor. An example template has been provided. When creating your own templates,
they should be .txt files with any customizable fields placed inside double-brackets ex. {{}}.

You will need to install pyperclip. For instructions go to https://github.com/asweigart/pyperclip.
