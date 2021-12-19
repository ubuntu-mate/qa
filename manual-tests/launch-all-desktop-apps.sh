#!/bin/bash

sigint_callback() {
    killall tail;
    echo;
    echo;
    echo "Killed, exiting";
    
    exit 1
}

trap 'sigint_callback' SIGINT

for fd in $(dpkg -S ".desktop" | grep "\.desktop$" | awk '{print $2}' | sort -u | grep -v "^/etc")
do 

    p=$(basename -- $fd)
    echo "[i] Clearing ~/.xsession-errors log-file";    
    > ~/.xsession-errors
    
    echo "[i] Will now launch \"$p\" ($fd) application";
    echo "[i] The output of \"tail -f ~/.xsession-errors\" is below:";
    tail -f ~/.xsession-errors & 
    
    echo ""
    
    if grep -E "NoDisplay=true|Hidden=true|NotShowIn=.*MATE" $fd 
    then
        echo "   ... skip as hidden."
    else
        if grep -E "Exec=|TryExec=" $fd
        then
            echo "   ... run."
            gtk-launch $p &
        else
            echo "   ... skip as having no Exec."
        fi
    fi

    read -n1 -p "[!] Press any key to launch next application";

    killall tail;
    clear

done

exit 0
