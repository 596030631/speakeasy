def print_hi(question):
    print(f'Hi, {question}')  # Press Ctrl+F8 to toggle the breakpoint.
    answer = "I am fine."
    return answer

def print_Batman(question):
    print(f'Hi answer of {question}')
    answer = 'Hi answer of '+ question +  'is Lorenzo Semple, Jr.'
    return answer

def print_Daniel(question):
    answer = 'the answer is yes'
    return answer

#I am a big fan of Steven Spielberg, could you recommend some of his action movies?
def print_Spielberg(question):
    answer= 'Saving Private Ryan'
    return answer

#I like the Jurassic Park movie; can you recommend any similar movies?
def print_Jurassic(question):
    answer='The Lost World: Jurassic Park , Jurassic Park III, Tyrannosaur, Jurassic World '
    return answer

#What is the name of the lead actor in the movie Catch Me If You
def print_Catch(question):
    answer='Karan'
    return answer
if __name__ == '__main__':
    answer = print_hi('How are you?')
    print(answer)
