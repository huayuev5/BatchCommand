#!/usr/bin/expect
set timeout 10
set host [lindex $argv 0]
set username [lindex $argv 1]
set password [lindex $argv 2]
spawn ssh $username@$host
expect {
    "(yes/no)?" {
        send "yes\n"
        expect "*assword": {send "$password\n"}
        exp_continue
    }
    "*assword:" {
        send "$password\n"
        exp_continue
    }
    "*Last login:*" {
        send "chmod +x ljx_batch_excute.sh \r"
        send "./ljx_batch_excute.sh \r"
        send "logout \r"
        interact
    }
}
