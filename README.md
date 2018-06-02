# asymmetrik-coding-challenge

How To Test:

1. Download a python IDE, or follow the instructions at https://www.pythoncentral.io/execute-python-script-file-shell/ to run the program in command prompt.
2. Run the main.py file.
3. Enter 1. This will prompt you to enter in a passage.
4. Enter 2. This will prompt you to enter in a fragment and retrieve the words that would autocomplete the fragment.
5. Enter 0 at any time to quit the process. Enter 3 at any time to clear the words.

Test Cases:
1. Test words without punctuation
2. Test words with punctuation on the front and back and that are not in the blacklist. Make sure the punctuation gets stripped. Dashes and apostrophes should stay in the word.
3. Alternate between steps 3 and 4 in How To Test to make sure that words being entered later are following tiebreaker rules.
	E.g. There are 3 "the"'s and 2 "there"'s in the program. Train the program with a "there".
			Enter the fragment "th". The word "there" should return first since it was the most recent "th-" prefix word to break the tie of both words having a count of 3.