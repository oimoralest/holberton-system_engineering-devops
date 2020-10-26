# 0x05. Processes and signals

## Description

    This porject is about processes and signals in bash

## Content

| File | Description |
| --- | --- |
| [0-what-is-my-pid](./0-what-is-my-pid) | script that displays its own PID |
| [1-list_your_processes](./1-list_your_processes) | script that displays a list of currently running processes |
| [2-show_your_bash_pid](./2-show_your_bash_pid) | script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process |
| [3-show_your_bash_pid_made_easy](./3-show_your_bash_pid_made_easy) | script that displays the PID, along with the process name, of processes whose name contain the word `bash` |
| [4-to_infinity_and_beyond](./4-to_infinity_and_beyond) | script that displays `To infinity and beyond indefinitel` |
| [5-dont_stop_me_now](./5-dont_stop_me_now) | script that stops `4-to_infinity_and_beyond process` |
| [6-stop_me_if_you_can](./6-stop_me_if_you_can) | script that stops `4-to_infinity_and_beyond process` |
| [7-highlander](./7-highlander) | script that displays:
- `To infinity and beyond` indefinitely
- With a `sleep` 2 in between each iteration
- `I am invincible!!!` when receiving a SIGTERM signal |
| [8-beheaded_process](./8-beheaded_process) | script that kills the process `7-highlander` |

## Requeriments

- All the scripts were interpreted on Ubuntu 14.04
- All the scripts were checked with shellcheck version 0.4.6
