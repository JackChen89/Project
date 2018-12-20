changeway=input()
sentence=input().split(" ")

if changeway=="R":
	if "not" not in sentence:
		if "are" in sentence:
			index=sentence.index("are")
			sentence[index]="are not"

		if "is" in sentence:
			index=sentence.index("is")
			sentence[index]="is not"

		if "am" in sentence:
			index=sentence.index("am")
			sentence[index]="am not"

	else:
		sentence.remove("not")

if changeway=="Q":
	if "not" not in sentence:
		if "are" in sentence:
			index=sentence.index("are")
			sentence[index-1]=sentence[index-1].lower()
			sentence[index]=sentence[index-1]
			sentence[index-1]="Are"

		if "is" in sentence:
			index=sentence.index("is")
			sentence[index]=sentence[index-1].lower()
			sentence[index-1]="Is"

		if "am" in sentence:
			index=sentence.index("am")
			sentence[index]=sentence[index-1]
			sentence[index-1]="Am"

	else:
		if "are" in sentence:
			index=sentence.index("are")
			sentence[index-1]=sentence[index-1].lower()
			sentence[index]=sentence[index-1]
			sentence[index-1]="Aren't"
			sentence.remove("not")
		if "is" in sentence:
			index=sentence.index("is")
			sentence[index]=sentence[index-1].lower()
			sentence[index-1]="Isn't"
			sentence.remove("not")
		if "am" in sentence:
			index=sentence.index("am")
			sentence[index]=sentence[index-1]
			sentence[index-1]="Amn't"
			sentence.remove("not")

for word in sentence:
	if sentence.index(word)!=len(sentence)-1:
		print(word,end=" ")
	else:
		print(word,end="")	