

def remove_polish_characters(text):
	new_text = ''

	polish_characters = {
		'ą': 'a',
		'ć': 'c',
		'ę': 'e',
		'ł': 'l',
		'ń': 'n',
		'ó': 'o',
		'ś': 's',
		'ź': 'z',
		'ż': 'z'
	}

	for index in range(len(text)):
		if text[index] in ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']:
			new_text = new_text + polish_characters[text[index]]
		else:
			new_text = new_text + text[index]

	return new_text