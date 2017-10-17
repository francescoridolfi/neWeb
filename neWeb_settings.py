class settings:
    host = ''
    port = 80

    title = "A new neWeb framework's projects!"

    runnable_files = ["index.html"]

    paths = {
        '/': {"status": 200},
        '/main.css': {"status": 200},
    }

    resp = {
        500: 'This path not work!',
        404: 'ERROR: This path was not found!',
        '/': "index.html",
        '/main.css': "main.css",
    }