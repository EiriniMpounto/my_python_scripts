# Author of this file @EiriniMpounto

This particular file contains all the main knowledge for a Data Scientist in pyhton.

## GENERAL INSTRUCTIONS FOR PYTHON
Before one starts coding and building and algorithm, whether she/he is a Data Scientist or not, it is always better to understand the the phylosophy of python. First I am going to portray the following lines written by Tim Peters about the Zen of programming. You can also find his words by typing the following command and run it: import this

The result would be:
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


Now that we have set the philosophy of coding we should set some basic ground rules on how to make your code more readable.
1. The name of the files should always be on lower case and seperated by the '_' symbol, e.g: dat_cleaner
2. Using comments into your code is extremely helpful. But a lot of comments cam sometimes confuse the person that is reading your code. Therefore after cleaning make sure to remove any comments that are not important.
3. It is at most handy to use the PEP-8 style when writing your code and naming your variables: For instance the name of a class should be written as following: CapWord and the name of a function: cap_word.
4. Also using black format can also be handy in order to pretify your code: you first need to pip install black and then to write the following command into your terminal: $ black [file or directory]