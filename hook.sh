pyplate () {
    function liner() {
        echo "Usage: pyplate.sh [OPTIONS]"
        echo "Options:"
        echo "  -h, --help     Display this help message"
        echo "  --version      Show the script version"
        echo "  script [DIR]   Generate an script style project inside DIR (will make dir if it does not exist)"
        echo "  notebook [DIR] Generate a notebook style project inside DIR (will make dir if it does not exist)"
    }
    # Check if no arguments are provided
    if [ "$#" -eq 0 ]; then
        liner
        return 1
    fi
    while [[ "$1" != "" ]]; do
        case $1 in
            -h )
                liner
                return 0
                ;;
            --help )
                liner
                return 0
                ;;
            --version )
                echo "Script Version 1.0"
                return 0
                ;;
            script | notebook)
                template="$HOME/Templates/Pyplates/$1"
                dest="$2"
                mkdir -p "$dest"
                cp -r "$template/"* "$dest"
                return 0
                ;;
            * )
                echo "Invalid option: $1"
                liner
                return 1
        esac
        shift
    done
}

alias pyplates=pyplate
