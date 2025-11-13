pyplate () {
    template="$HOME/Templates/Pyplates/$1"
    dest="$2"
    mkdir -p "$dest"
    cp -r "$template/"* "$dest"
}
