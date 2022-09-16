word = input('Executioner, choose a word: ')

def guess_and_check():

    def reveal_word():
        list_word = list(word)
        index = list_word[len(list_word) -1] 
        blank_list = [] 
        for i in list_word:
            blank_list.append('__') 
        #print(blank_list)
        letter_count = list_word.count(letter) 
        print('letter count is ', letter_count)

        def help_reveal(index):
            index = range(0, len(word))
            if list_word[index] == letter:
                blank_list[index] = letter

        mixed_list = list(map(help_reveal, list_word))
        print(mixed_list)      
                

    letter = input('Condemned, choose a letter: ')
    if word.__contains__(letter):
        print('The letter is in the word')
        #here we need something that will return an index 
        reveal_word()
        return 1
    else:
        print('The letter is not in the word')
        reveal_word()
        return 0

life = 9 
while life > 0:
    if guess_and_check() == 0:
        life -= 1
        print('You have ', life, 'life left')
    if life <= 0:
        print('Player 2 you lose')

