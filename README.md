# sentence-generator

Simple python script which generates a random sentence based on what verbs/nouns/etc. are provided in the corresponding files. Also applies basic english logic, so that words are dynamically fitted to be more valid in terms of grammar. The sentences are nonsensical, which is both a "bug" and a feature, in that I didn't intend for it to be buggy (thanks to computers not understanding the nuance of human speech), but I also found it rather entertaining and decided to stick with it due to the unique gibberish it managed to generate.

Originally used for my [random meme generator](https://www.youtube.com/channel/UCLyK-hcEoqZGaYTosRT-rug) (now discontinued), but I figured that rather than deleting this it would probably serve better to fashion it as a more general-purpose library of sorts. Which would probably help when I move on to do more personal projects.

Pretty much all the functions are free to be used by you. And if you execute the python script through python, you'll be greeted with a neat interface to dynamically generate sentences. Thought it might be useful rather than having it close on you.

There might be a library that already does this, but if not, then here ya go. :)


## Noun starting word rules

So incase you would like to add your *own* nouns to the mix (you shouldn't have to given the vast abundance of them, but if you would like to then it's fine by me), there are special formatting rules you can ask the program to follow by simply appending a letter in parantheses after the noun (**WITH NO SPACES BETWEEN THE MARKER AND THE NOUN ITSELF**)

Like this for example: hello(T)
**NOT** like this: hello (T)

The formatting rules are as follows:
* **(T)** -> Adds "the" infront of the noun (Ex: pen(T) turns to "the pen")
* **(P)** -> Adds *nothing* infront of the noun, which is mainly useful for proper nouns, hence why "P" is the letter. (Ex: George(P) turns to "George")
* **(R)** -> Replaces itself with (T) or (P) each time the noun is run in the script, with a random chance of each occuring.
* **default** -> Adds "a" or "an" infront of the noun, depending on if it starts with a vowel or a consonant (Ex: "apple" turns to "an apple")

Feel free to add your own custom formats if you'd like (it's in the `formatting_rules` array on line 81). Though I think these formats might be enough for most people.
