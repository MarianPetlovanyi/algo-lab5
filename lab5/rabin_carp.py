def rabin_karp_algo(pattern, txt, divider = 101):
	base = 256
	pattern_length = len(pattern)
	text_length = len(txt)
	pattern_str_hash = 0
	text_str_hash = 0
	hash_num = 1

	for i in range(pattern_length-1):
		hash_num = (hash_num*base) % divider

	for i in range(pattern_length):
		pattern_str_hash = (base*pattern_str_hash + ord(pattern[i])) % divider
		text_str_hash = (base*text_str_hash + ord(txt[i])) % divider

	j = 0
	positions = list()
	for i in range(text_length-pattern_length+1):
		if pattern_str_hash == text_str_hash:
			for j in range(pattern_length):
				if txt[i+j] != pattern[j]:
					break
				else:
					j += 1

			if j == pattern_length:
				#print("Index " + str(i))
				positions.append(i)

		if i < text_length-pattern_length:
			text_str_hash = (base*(text_str_hash-ord(txt[i])*hash_num) + ord(txt[i+pattern_length])) % divider

	return positions

if __name__ == '__main__':
	txt = "Lorem Ipsum is simply dummy text of the printing and typesetting industry." \
                         " Lorem Ipsum has been the industry's standard dummy text ever since the 1500s," \
                         "when an unknown printer took a galley of type and scrambled" \
                         " it to make a type specimen book.It has survived not only five centuries," \
                         " but also the leap into electronic typesetting,remaining essentially unchanged." \
                         "It was popularised in the 1960s with the release of Letraset sheets containing" \
                         " Lorem Ipsum passages,and more recently with desktop publishing softwarelike Aldus" \
                         " PageMaker including versions of Lorem Ipsum. Marian Petlovanyi"
	pattern = "Lorem"
	divider = 101
	result = rabin_karp_algo(pattern, txt)
	print(result)
