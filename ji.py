import pyttsx3


a = [2,7,4,9,3]
rohit = pyttsx3.init()
rohit.say("your list is ")
rohit.say(a)

rohit.say("your sort list is ")
rohit.say(sorted(a))

print(a[3])
rohit.runAndWait()