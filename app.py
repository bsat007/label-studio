from label_studio.server_ import input_args, app

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=input_args.port)
