if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi

PS1='\033[1;37m╭╾╼「\033[1;92m \date \033[1;37m」\033[34;1m[\w]\033[1;90m•\033[35;1m©AmmarBN\033[1;37m╼╾
╰─❥ '
