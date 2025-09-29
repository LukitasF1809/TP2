#!/bin/bash

todo=1

read -p "apreta '5' para ejecutar la creacion del entorno para la pagina, apreta cualquier otra boludez para cancelar: " i

if [ "$i" != "5" ]; then
    echo "mira que sos bobo eh, nos vemos"
    
else
    for dir in static templates app; do
                        if [ ! -d "./pagina/$dir" ]; then
                            todo=0
                            break
                        fi
                    done
                    if [ ! -f "./pagina/app/app.py" ]; then
                        todo=0
                    fi

                    if [ "$todo" -eq 1 ]; then
                    echo "el entorno ya fue creado"
                    else
                    
                        echo -n "creando enotrno"

                        mkdir -p ./pagina/{app,templates,static/{css,images}}
                        touch ./pagina/app/app.py
                        touch ./pagina/templates/home.html
                        touch ./pagina/static/styles.css
                        touch ./pagina/.env
                        sleep 0.5
                        echo -n "."
                        
                        sleep 0.5
                        
                        echo -n "."

                        python3 -m venv ./pagina/.venv
                        source ./pagina/.venv/bin/activate
                        pip install flask flask_mail python-dotenv

                        sleep 0.5
                        echo "."



                        todo=1
                        echo "entorno creado!"
                fi
fi