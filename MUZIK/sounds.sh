#!/bin/bash

if [[ $# == 1 ]]; then
    case "$1" in 
	POW)
	    echo "{POW}";
	    paplay /usr/local/lib/python2.7/dist-packages/pygame/examples/data/punch.wav
	    ;;
	Good) 
	    echo "Excellent"; 
	    paplay /lib/live/mount/rootfs/filesystem.squashfs/usr/share/metasploit-framework/data/sounds/default/excellent.wav
	    ;;
	try)
	    echo "TRY HARDER!";
	    paplay /lib/live/mount/rootfs/filesystem.squashfs/usr/share/metasploit-framework/data/sounds/default/try_harder.wav
	    ;;
	YES)
	    echo "Wonderful";
	    paplay /lib/live/mount/rootfs/filesystem.squashfs/usr/share/metasploit-framework/data/sounds/default/wonderful.wav
	    ;;
	BOOM)
	    echo 'Boom'
	    paplay /usr/local/lib/python2.7/dist-packages/pygame/examples/data/boom.wav
	    ;;
	success)
	    echo "Success"
	    paplay /lib/live/mount/rootfs/filesystem.squashfs/usr/share/metasploit-framework/data/sounds/default/exploit_worked.wav
	    ;;

    esac
fi
#paplay /usr/share/sounds/sound-icons/trumpet-12.wav
#paplay /usr/share/sounds/sound-icons/percussion-10.wav
#paplay /usr/share/sounds/sound-icons/prompt.wav
