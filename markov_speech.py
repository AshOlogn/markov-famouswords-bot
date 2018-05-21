import sys
import praw
import random
 
#input text
input_text = {}
message_info = "\n~ Randomly generated using Markov methods from material by a significant figure"

#returns string from sliding window
def get_history_string(sliding_window, input_index=0):
  length = len(sliding_window)
  index = input_index
  final_string = ["a"]*length
  for i in range(length):
    final_string[i] = sliding_window[index % length]
    index += 1
  return ' '.join(final_string)    
    
#generates hashmap from list of words to possible successors
def create_markov_table(person='lincoln', n=5):
  hashmap = {}
  sliding_window = ['a']*n
  s = []
  
  with open(person + '.txt', 'r') as f: 
  
    global input_text
    s = f.read().split()
    input_text[person] = s
    index = 0
    
    for word in s:
      #add to hashmap
      if index >= n:
        history = get_history_string(sliding_window, index)
        if history in hashmap:
          hashmap[history].append(word)
        else:
          hashmap[history] = [word]
      
      sliding_window[index % n] = word
      index += 1
  
  return hashmap
        
        
def generate_text(hashmaps, person='lincoln', n=5, output_length=300):
  #pick a random seed to build output from
  global input_text
  rand_index = random.randint(0, len(input_text[person])-n)
  output = input_text[person][rand_index:rand_index+n]
  hashmap = hashmaps[person]
  
  #grow the output
  for i in range(output_length-n):
    history = ' '.join(output[-n:])
    output.append(random.choice(hashmap[history]))
  
  return ' '.join(output)

def main():

  #default values
  n = 5 #history length (words)
  output_length = 300 #output text length
  monitor_subreddit = 'testingground4bots'
  
  #gather command line arguments (if present)
  args_list = sys.argv
  if len(args_list) == 2:
    monitor_subreddit = args_list[1]
  elif len(args_list) == 3:
    monitor_subreddit = args_list[1]
    n = int(args_list[2])
    output_length = int(args_list[3])
  elif len(args_list) != 1:
    print("Incorrect number of command line arguments\nAcceptable args: <Markov history length> <Output length (words)>")
    sys.exit(1)
    
  #gather list of people to generate text for
  people = []
  with open('_people.txt') as f:
    for person in f.readlines():
      #exclude people that are "commented out"
      if person[0:2] != '//':
        people.append(person.strip())
  
  bot = praw.Reddit(client_id='',
                       client_secret= '',
                       password= '',
                       user_agent='',
                       username='')
  
  hashmaps = {}
  for person in people:
    hashmaps[person] = create_markov_table(person, n)
  
  subreddit = bot.subreddit(monitor_subreddit)
  comments = subreddit.stream.comments()
  
  #for all comments with trigger word, reply with random text
  for comment in comments:
    text = comment.body
    for person in people:
      if "!" + person in text:
        comment.reply(generate_text(hashmaps, person, n=n, output_length=output_length) + message_info)
      
if __name__ == '__main__':
  main()
  
  
  
