alias ll="ls -lah"

# set python to python2
#alias python="`which python2`"

alias video.play="mpv --no-config --vo=tct "
alias image.play="chafa "

alias clean.history="cat /dev/null > ~/.bash_history && history -c && exit"
#alias clean.video.all='find / \( -name "*.vob" -o -name "*.mp4" \) |xargs rm'
alias clean.video.all='find / -regextype posix-egrep -regex ".*\.(mp4|vob)$" | xargs rm'
alias clean.audio.all='find / -regextype posix-egrep -regex ".*\.(wav|mp3)$" | xargs rm'

# csvtool readable filename | view -
alias csv.display=""
alias chk.size="du -hs"

alias chk.os="cat /etc/issue.net && cat /etc/debian_version"

## check which ports are being used by a certain app
## or check which app is using a specific port
alias app2port='f(){ lsof -i | grep "$@";  unset -f f; }; f'

## unset all proxies
alias unset.proxy="unset all_proxy && unset ALL_PROXY"

## show only non-empty subfolders
alias ls.non-empty="f(){ find \"\$@\" -mindepth 1 -type d -exec du -s {} + | awk '\$1 > 4'; }; f"

# check if any line of arg2 contains any line of arg1
chk.txtintxt () {
    echo "Usage:   chk.txtintxt <filename1> <filename2>"
    echo "Example: chk.txtintxt pypi.pkg.lst pypi.malicious.lst"

    # Check if the number of arguments is two
    if [ $# -eq 2 ]; then
        # Do something with the arguments
        echo "The first argument is $1 and the second argument is $2"
        cat $1|egrep `concatstr "|" $2`;
    else
        # Print an error message and exit with status code 1 (failure)
        echo "This function requires two arguments" >&2
        exit 1
    fi
}
chk.txtinpip () {
    echo "Usage:   chk.txtinpip <filename>"
    echo "Example: chk.txtinpip pypi.pkg.lst"
    # Check if the number of arguments is zero
    if [ $# -eq 0 ]; then
        # Exit with status code 1 (failure)
        echo "This function requires one argument"
        exit 1
    else
        items=`concatstr '|' $1`
        pip list|egrep $items;
        exit 0
    fi    
}

# find all pypi lib version candidate
chk.whl.cache () {
    if [ $# -eq 0 ]; then
        pip cache list
    else
        pip cache list |grep $1
    fi
}
