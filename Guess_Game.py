import random


def check_attempt(word, remain_attempts, check):
    '''
    check attempts
    '''
    if check:
        get_input(word, remain_attempts)
    else:
        remain_attempts -=1
        print('Remaining attempts:',remain_attempts)
        get_input(word, remain_attempts)


def valid_guess(user_guess, word, index_val):
    '''
    Update current word with specific index value
    '''
    input_index = word.index(user_guess)
    index_val.update({input_index:user_guess})  # index
    cur_word = ''
    for i in range(len(word)):
        if i in index_val.keys():
            cur_word+=index_val.get(i)
        else:
            cur_word+='*'
    print('Word:',cur_word)
    return index_val, cur_word


def invalid_guess(user_guess, wrong_guess, remain_attempts):
    if user_guess in wrong_guess:
        print('Remaining attempts:',remain_attempts)
        get_input(word, cur_word, index_val, wrong_guess, remain_attempts)
    else:
        wrong_guess.append(user_guess)
        remain_attempts-=1
        print('Remaining attempts:',remain_attempts)
        return wrong_guess, remain_attempts


def is_valid(user_guess):
    if user_guess.isnumeric():
        print('Input must be a letter')
        return False
    else:
        if len(user_guess)==1:
            return True
        else:
            print('Input length must be 1')
            return False


def get_input(word, cur_word, index_val, wrong_guess, remain_attempts):
    if cur_word==word:
        print('You Won!')
    elif remain_attempts == 0:
        print('Game Over.')
    else:
        user_guess = str(input('Input ur guess :'))
        if is_valid(user_guess):
            if user_guess in word:
                index_val, cur_word = valid_guess(user_guess, word, index_val)
                get_input(word, cur_word, index_val, wrong_guess, remain_attempts)
            else:
                wrong_guess, remain_attempts = invalid_guess(user_guess, wrong_guess, remain_attempts)
                get_input(word, cur_word, index_val, wrong_guess, remain_attempts)
        else:
            print('Remaining attempts:',remain_attempts)
            return get_input(word, cur_word, index_val, wrong_guess, remain_attempts)


def generate_random():
    # generate one random word from collection
    collection = ['number', 'lot', 'set', 'store', 'cluster', 'batch',
                  'digest', 'clump', 'combine', 'hoard', 'crowd', 'pile',
                  'company', 'kit', 'levy', 'master', 'kid', 'pair',
                  'lot', 'stock', 'stack', 'secure', 'index', 'goal',
                  'home', 'key', 'public', 'get', 'private', 'focus'
                  ]
    try:
        word = random.choice(collection).lower()
        remain_attempts = len(word) * 2
        print('Remaining attempts:', remain_attempts)
        cur_word = word[0]
        index_val = {0: cur_word}
        for i in range(len(word) - 1):
            cur_word += '*'
        print('Word:', cur_word)
        wrong_guess = []
        get_input(word, cur_word, index_val, wrong_guess, remain_attempts)
    except:
        print('Restarting...')
        generate_random()


generate_random()

