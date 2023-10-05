alias ll="ls -l"

alias clean.history="cat /dev/null > ~/.bash_history && history -c && exit"
#alias clean.video.all='find / \( -name "*.vob" -o -name "*.mp4" \) |xargs rm'
alias clean.video.all='find / -regextype posix-egrep -regex ".*\.(mp4|vob)$" | xargs rm'
alias clean.audio.all='find / -regextype posix-egrep -regex ".*\.(wav|mp3)$" | xargs rm'

alias video.play="mpv --no-config --vo=tct "
alias image.play="chafa "

# csvtool readable filename | view -
alias csv.display=""
alias chk.size="du -hs"

alias chk.os="cat /etc/issue.net && cat /etc/debian_version"
