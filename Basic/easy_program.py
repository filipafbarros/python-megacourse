#!/usr/bin/env python3

def main():
	array = []
	while True:
		prompt = input("Say something: ")
		if (prompt == "\\end"):
			break
		else:
			array.append(prompt)
			continue
	format(array)
	return


def format(words):
	new_array = []
	for word in words:
		new_word = word[0].upper() + word[1:] + '.'
		new_array.append(new_word)
	full_sentence = ' '.join(new_array)
	print(full_sentence)

if __name__ == "__main__":
	main()





