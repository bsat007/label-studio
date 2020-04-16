from label_studio.server import app, input_args

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=input_args.port, debug=input_args.debug)
