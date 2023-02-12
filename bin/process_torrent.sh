#!/bin/zsh
#
# Copies a directory with a movie file to the FreeBSD server for storage
#

# global variables
message=""
previous_message=""
timestamp=$(date -u +%F\ %T)
logrepeat=0
active_user=""

function get_active_user() {
    #   Collect current logged in user
    active_user=$(echo "show State:/Users/ConsoleUser" | scutil | awk '/Name :/ && ! /loginwindow/ { print $3 }')
}

function print_log() {
    #   Print a log message to standard output and system log
    message="${*}"
    timestamp=$(date -u +%F\ %T)

    get_active_user
    if [[ -z "${message}" ]]; then
      return
    elif [[ "${message}" == "${previous_message}" ]]; then
        ((logrepeat = logrepeat + 1))
        return
    elif [[ ($logrepeat -gt 0) && ("$message" != "$previous_message") ]]; then
        echo "$timestamp:${active_user}[$$] : Last message repeated {$logrepeat} times"
        logger -i "Last message repeated {$logrepeat} times"
        logrepeat=0
    elif [[ $logrepeat -eq 0 ]]; then
        echo "$timestamp:${active_user}[$$] : $message"
        logger -i "$message"
        say "$message"
        previous_message="$message"
    fi
}


if [[ -n "$1" ]]; then
  torrentpath=$1
elif [[ -n "$3" ]]; then
  torrentid=$1
  torrentname=$2
  torrentpath=$3
elif [[ -n "$TR_TORRENT_DIR" ]]; then
  torrentpath="$TR_TORRENT_DIR"
else
  print_log "Usage: $0 <folder name>"
  exit 1
fi

if [[ -d "$torrentpath" ]]  && ls $torrentpath/*.mkv || ls $torrentpath/*.avi || ls $torrentpath/*.mp4; then
    print_log "Processing $torrentpath"
    sleep 60
    print_log "Starting Transfer" && output=$(scp -r "$torrentpath" rdottin@192.168.1.188:/zroot/movies/completed-movies) && print_log "$output" && output=$(rm -vfr "$torrentpath") && print_log "$output" && print_log "Transfer Complete"
    return_code="$?"
    if [ "$return_code" -ne  "0" ]; then
      print_log "Return code is $return_code"
      print_log "An error occurred."
    fi
eLse
  print_log "Unable to find video file in $torrentpath."
fi

if [[ -n "$previous_message" ]]; then
  print_log
fi
