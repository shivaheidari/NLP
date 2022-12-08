import re
import long_responses as long
#define a function which calculates the probability of each answer

def message_probability(user_message, recognize_words,single_responce=False,required_words=[] ):
    message_certainty=0
    has_required_words=True

    for word in user_message:
        if word in recognize_words:
            message_certainty+=1

    percentage=float(message_certainty)/float(len(recognize_words))

    for words in required_words:
        if words not in user_message:
            has_required_words=False
            break
    if has_required_words or single_responce:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list={}


    def response(bot_response,list_of_words,single_response=False,requirred_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]=message_probability(message,list_of_words,single_response,requirred_words)

    response("hello!",['hello','hi','hola','salam','hey'],single_response=True)
    response("I am doing fine and you",['how',"are","you","doing"],requirred_words=["how"])
    response("Thank you",["i",'love',"you"])
    best_match=max(highest_prob_list,key=highest_prob_list.get)
    print(highest_prob_list)
    return best_match
def get_response(user_input):

    split_message=re.split(r'\s+|[,;?.-]\s',user_input.lower())
    response=check_all_messages(split_message)
    return response

while True:
    print("Bot: "+get_response(input("You: ")))

