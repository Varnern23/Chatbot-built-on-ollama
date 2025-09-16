import ollama
from datetime import datetime
from datetime import date
import os
def query_ollama(prompt: str, model: str) -> str:
    """Call Ollama with the user prompt and return the reply text."""
    try:
        response = ollama.chat(model=model,
                               messages= [{"role": "user",
                                           "content": prompt}],
                                           stream=True)
        final =""
        for chunk in response:
            print(chunk['message']['content'], end='', flush=True)
            final+=chunk['message']['content']
        return final
    except ollama.ResponseError as e:
        print("Error: ", e.error)
def main() -> None:
    #os.makedirs(f"/home/nathan.varner/Documents/DSC-360/Lab01/{date.today()}")
    with open(f"/home/nathan.varner/Documents/DSC-360/Lab01/Transcript"+ f"{datetime.now()}" +".txt", "a") as f:
        MODEL = "gemma3:1b" 
        print("Ollama booting......\n type /exit to end session /model <model> to change models and /new to wipe the memory")
        j = query_ollama("Introduce yourself to the user", MODEL)
        y = 1
        x= "[" + MODEL + "]" + j
        f.write(f"[{datetime.now()}]"+"[" + MODEL + "]" + j + "\n")
        PROMPT= ""
        while y == 1:
            PROMPT = input("\n")
            x += "\n[" + MODEL + "]" + j+"\n[USER]"+PROMPT
            f.write(f"[{datetime.now()}]"+"[" + "USER" + "]" + PROMPT + "\n")
            if PROMPT == "/exit":
                y=2
            if PROMPT == "/new":
                x = ""
                print("memory has been reset")
                f.write(f"[{datetime.now()}]"+"[" + "SYSTEM" + "]" + "Memory reset" + "\n")
            test = PROMPT.split()
            if test[0] == "/model":
                MODEL = test[1]
            j=query_ollama(x + PROMPT, MODEL)
            f.write(f"[{datetime.now()}]"+"[" + MODEL + "]" + j + "\n")

    
if __name__ == "__main__":
    main()