import os,sys,time,requests
os.system("clear")
IP = requests.get('https://api.ipify.org').text
localtime = time.asctime(time.localtime(time.time()))
print ("""
\033[1;95m╔╦╗\033[1;97m┌─┐┬─┐┌┬┐┬ ┬─┐ ┬  \033[1;95m╔╦╗\033[1;97m┌─┐┌┬┐
\033[1;95m ║ \033[1;97m├┤ ├┬┘││││ │┌┴┬┘  \033[1;95m║║║\033[1;97m│ │ ││
\033[1;95m ╩ \033[1;97m└─┘┴└─┴ ┴└─┘┴ └─  \033[1;95m╩ ╩\033[1;97m└─┘─┴┘
    [\033[1;0m\033[1;41mCoded By AmmarBN\033[1;0m]
────────────────────────────────────────────────────""")
print ("""     \033[1;97m[\033[1;90m~\033[1;97m] Creator: \033[1;92mAmmarBN
     \033[1;97m[\033[1;90m~\033[1;97m] Github: \033[1;92mgithub.com/Lord-Ammar""")
print ("     \033[1;97m[\033[1;90m~\033[1;97m] Time: \033[1;92m"+localtime)
print ("     \033[1;97m[\033[1;90m~\033[1;97m] Ip: \033[1;92m"+IP)
print("")
