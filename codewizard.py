import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import openai
import threading
import os 
from dotenv import load_dotenv
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# ------------------- OpenAI Client -------------------
#client = openai.OpenAI(api_key="")  # Replace with your key

# ------------------- Main App -------------------
"""class CodeWizardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Wizard")
        self.root.geometry("900x700")
        self.root.configure(bg="#1e1e1e")

        # Make the main grid responsive
        self.root.rowconfigure(2, weight=1)  # Input code area
        self.root.rowconfigure(5, weight=2)  # Output code area
        self.root.columnconfigure(0, weight=1)

        # Target Language
        self.languages = ["Python", "JavaScript", "C++", "Java", "Go"]
        self.target_lang = tk.StringVar(value="JavaScript")

        ttk.Label(root, text="Target Language:", foreground="#fff", background="#1e1e1e").grid(row=0, column=0, sticky="w", padx=10, pady=(10,0))
        self.lang_frame = tk.Frame(root, bg="#1e1e1e")
        self.lang_frame.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        for lang in self.languages:
            b = ttk.Radiobutton(
                self.lang_frame,
                text=lang,
                value=lang,
                variable=self.target_lang
            )
            b.pack(side="left", padx=5, pady=5)

        # Input Code
        ttk.Label(root, text="Input Code:", foreground="#fff", background="#1e1e1e").grid(row=2, column=0, sticky="w", padx=10)
        self.input_text = scrolledtext.ScrolledText(root, bg="#252526", fg="#d4d4d4", insertbackground="#fff", font=("Consolas", 12))
        self.input_text.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

        # Buttons + Status
        self.button_frame = tk.Frame(root, bg="#1e1e1e")
        self.button_frame.grid(row=4, column=0, sticky="ew", padx=10, pady=5)
        self.button_frame.columnconfigure((0,1,2), weight=1)

        self.status_label = ttk.Label(self.button_frame, text="", foreground="#fff", background="#1e1e1e")
        self.status_label.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(5,0))

        ttk.Button(self.button_frame, text="Convert", command=lambda: self.call_backend("convert")).grid(row=0, column=0, sticky="ew", padx=5)
        ttk.Button(self.button_frame, text="Fix", command=lambda: self.call_backend("fix")).grid(row=0, column=1, sticky="ew", padx=5)
        ttk.Button(self.button_frame, text="Run", command=lambda: self.call_backend("run")).grid(row=0, column=2, sticky="ew", padx=5)

        # Output Code
        ttk.Label(root, text="Output:", foreground="#fff", background="#1e1e1e").grid(row=5, column=0, sticky="w", padx=10)
        self.output_text = scrolledtext.ScrolledText(root, bg="#1e1e1e", fg="#d4d4d4", font=("Consolas", 12))
        self.output_text.grid(row=6, column=0, sticky="nsew", padx=10, pady=5)

        # Make output text expandable
        root.rowconfigure(6, weight=2)"""

class CodeWizardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Code Wizard")
        self.root.geometry("950x750")
        self.root.configure(bg="#121212")

        # --- Custom Theme Setup ---
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "TLabel",
            background="#121212",
            foreground="#ffffff",
            font=("Segoe UI", 11)
        )
        style.configure(
            "TButton",
            font=("Segoe UI", 11, "bold"),
            padding=6
        )
        style.map(
            "TButton",
            background=[("active", "#6c63ff")],
            foreground=[("active", "#ffffff")]
        )

        # --- Target Language Selection ---
        ttk.Label(root, text="🎯 Target Language:").grid(row=0, column=0, sticky="w", padx=12, pady=(15, 5))

        self.languages = ["Python", "JavaScript", "C++", "Java", "Go"]
        self.target_lang = tk.StringVar(value="JavaScript")

        lang_frame = tk.Frame(root, bg="#121212")
        lang_frame.grid(row=1, column=0, sticky="w", padx=12, pady=5)
        for lang in self.languages:
            ttk.Radiobutton(lang_frame, text=lang, value=lang, variable=self.target_lang).pack(side="left", padx=5)

        # --- Input Code Section ---
        ttk.Label(root, text="🧩 Input Code:").grid(row=2, column=0, sticky="w", padx=12, pady=(10, 2))
        self.input_text = scrolledtext.ScrolledText(
            root, bg="#1e1e1e", fg="#dcdcdc",
            insertbackground="#ffffff", font=("Consolas", 12),
            wrap=tk.WORD
        )
        self.input_text.insert("1.0", "# Paste your code here...")
        self.input_text.grid(row=3, column=0, sticky="nsew", padx=12, pady=5)

        # --- Buttons ---
        button_frame = tk.Frame(root, bg="#121212")
        button_frame.grid(row=4, column=0, sticky="ew", padx=12, pady=10)
        button_frame.columnconfigure((0, 1, 2), weight=1)

        ttk.Button(button_frame, text="🪄 Convert", command=lambda: self.call_backend("convert")).grid(row=0, column=0, sticky="ew", padx=5)
        ttk.Button(button_frame, text="🩺 Fix", command=lambda: self.call_backend("fix")).grid(row=0, column=1, sticky="ew", padx=5)
        ttk.Button(button_frame, text="▶️ Run", command=lambda: self.call_backend("run")).grid(row=0, column=2, sticky="ew", padx=5)

        # --- Status Label ---
        self.status_label = ttk.Label(button_frame, text="", foreground="#ccc", background="#121212", font=("Segoe UI", 10))
        self.status_label.grid(row=1, column=0, columnspan=3, pady=(6, 0))

        # --- Output Code Section ---
        ttk.Label(root, text="📤 Output:").grid(row=5, column=0, sticky="w", padx=12, pady=(10, 2))
        self.output_text = scrolledtext.ScrolledText(
            root, bg="#1e1e1e", fg="#dcdcdc",
            font=("Consolas", 12), wrap=tk.WORD
        )
        self.output_text.insert("1.0", "# Output will appear here...")
        self.output_text.grid(row=6, column=0, sticky="nsew", padx=12, pady=5)

        # --- Responsive Layout ---
        for i in [3, 6]:
            root.rowconfigure(i, weight=1)
        root.columnconfigure(0, weight=1)
    # ------------------- Backend Logic -------------------
    def call_backend(self, mode):
        threading.Thread(target=self._call_backend_thread, args=(mode,), daemon=True).start()

    def _call_backend_thread(self, mode):
        self.status_label.config(text="Processing...")
        code = self.input_text.get("1.0", tk.END).strip()
        target_lang = self.target_lang.get()

        if not code:
            messagebox.showerror("Error", "Please enter some code first.")
            self.status_label.config(text="")
            return

        try:
            prompt = ""
            if mode == "run":
                prompt = f"Simulate running this code (auto-detect language) and show only the output or if it is asking input or to run gui code if correct  execpt its logic then make a file on that pc desktop and tell the user to run if he had that programming language installed in the user's desktop otherwise tell its error   :\n\n{code}"
            elif mode == "convert":
                syntax_prompt = f"Detect language automatically. Check this code for syntax errors only. Reply 'OK' if correct, otherwise list the errors:\n\n{code}"
                syntax_resp = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a syntax checker and if the error is logical or no error then give only that the code has no errors with converted targeted coding language.:\n\n{code}"},
                        {"role": "user", "content": syntax_prompt},
                    ],
                )
                syntax_result = syntax_resp.choices[0].message.content.strip()
                if syntax_result != "OK":
                    messagebox.showerror("Syntax Error", syntax_result)
                    self.status_label.config(text="")
                    return
                prompt = f"Detect language automatically and convert this code to {target_lang}:\n\n{code}"
            elif mode == "fix":
                prompt = f"Detect language automatically and fix syntax errors if the code have erros execpt logical errors otherwise throw that the code has no errors in this code:\n\n{code}"
            else:
                messagebox.showerror("Error", "Invalid mode")
                self.status_label.config(text="")
                return

            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert software developer. Provide only code/output without extra explanation."},
                    {"role": "user", "content": prompt},
                ],
            )
            result = completion.choices[0].message.content.strip()
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, result)

        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            self.status_label.config(text="")


# ------------------- Run App -------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = CodeWizardApp(root)

#this code works i think execept taking input if code takes input and i think gui
    root.mainloop() 

