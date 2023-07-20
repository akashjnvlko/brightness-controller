#!/bin/bash

# Determine the current directory
CURRENT_DIR=$(dirname "$(readlink -f "$0")")

# Create the desktop shortcut
echo "[Desktop Entry]" > bright.desktop
echo "Name=bright" >> bright.desktop
echo "Comment=Description of your app" >> bright.desktop
echo "Exec=$CURRENT_DIR/bright" >> bright.desktop
echo "Icon=$CURRENT_DIR/brightico.png" >> bright.desktop
echo "Terminal=false" >> bright.desktop
echo "Type=Application" >> bright.desktop
echo "Categories=Utility;Application;" >> bright.desktop

# Move the .desktop file to the appropriate location
DESKTOP_DIR="$HOME/.local/share/applications/"
mkdir -p "$DESKTOP_DIR"
mv bright.desktop "$DESKTOP_DIR"

