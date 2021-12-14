from logging import debug
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
#this line means the web server wont run when we just import stuff to and from but only when we run this python file(main) and (debug=True) means everytime we changes something inside our code, its gonna rerun the web server.
#wow my server is on lol: The address will show up in the terminal when running this file. But why does it say 404 tho. Yeah, that means ok.
#the website gonna get refresh everytime I saved the python file. 
#Ctrl+C and it will close the server