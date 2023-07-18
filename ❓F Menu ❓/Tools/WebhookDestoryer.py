import requests, threading

def print_pink(text):
    print("\033[95m" + text + "\033[0m")

desc = "Deletes a webhook"
params = {
    "webhook_url" : "the URL of the webhook you want to delete"
}

def run(webhook_url):
    requests.delete(webhook_url)
    print_pink("Webhook has been deleted!")

if __name__ == "__main__":
    config = {}
    for param in params:
        config[param] = input("\033[95mEnter " + params[param] + ": \033[0m")
    run(**config)
