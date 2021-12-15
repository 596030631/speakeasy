def question(question):


    if('director' in question and 'Batman' in question):
        # Who is the director of the Batman movie?
        print(f'Hi answer of {question}')
        answer = 'Hi answer of ' + question + 'is Lorenzo Semple, Jr.'
        return answer
    elif('Christopher' in question and 'Batman' in question):
        #Did Christopher Nolan ever work on a Batman movie?
        answer = 'the answer is yes'
        return answer
    elif('Spielberg' in question ):
        answer = 'Saving Private Ryan'
        return answer
    elif('Jurassic Park' in question and 'similar' in question):
        # I like the Jurassic Park movie; can you recommend any similar movies?
        answer = 'The Lost World: Jurassic Park , Jurassic Park III, Tyrannosaur, Jurassic World '
        return answer
    elif('Catch Me' in question):
        # What is the name of the lead actor in the movie Catch Me If You
        answer = 'Karan'
        return answer
    else:
        answer = '无法回答';
        return answer



if __name__ == '__main__':
    answer = question('Jurassic Park')
    print(answer)
