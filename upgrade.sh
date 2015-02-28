#!/bin/sh

opkg update
for i in `opkg list_installed | sed 's/ - .*//'`; do opkg upgrade $i; 
done
