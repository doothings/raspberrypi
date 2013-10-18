I wanted to be continually logged into IRC and also use it as a logging client for message on the [#doothings](irc://irc.freenode.net/doothings) IRC channel.

What better way than to use Raspberry Pi?

### Steps for using Raspberry Pi as IRC Client


1. We will use IRSSI, whici is a terminal based IRC client.

2. Install it by running ```sudo apt-get install irssi```

3. Also install ```screen``` by running ```sudo apt-get install screen```

4. ```screen``` and then press ```Enter```

5. ```irssi```

6. ```/server irc.freenode.net```

7. ```/join #doothings```

8. Now you have logged-in to the #doothings IRC Channel.

9. To Detach from the Client. Press ```Ctrl + a``` and then ```d```

10. You should be back to the terminal window.

11. To rejoin the IRC window write ```screen -r```
