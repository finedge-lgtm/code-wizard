"""import tkinter as tk
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
""" """class CodeWizardApp:
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
        root.columnconfigure(0, weight=1)""" """
"""#class CodeWizardApp:
   # def __init__(self, root):
  #      self.root = root
     #   self.root.title("✨ Code Wizard")
    #    self.root.geometry("950x750")
     #   self.root.configure(bg="#121212")

        # --- Custom Theme Setup ---
     #   style = ttk.Style()
     #   style.theme_use("clam")
     #   style.configure(
      #      "TLabel",
       #     background="#121212",
         #   foreground="#ffffff",
        #    font=("Segoe UI", 11)
       # )
      #  style.configure(
       #     "TButton",
       #     font=("Segoe UI", 11, "bold"),
       #     padding=6
       # )
      #  style.map(
      #      "TButton",
      #      background=[("active", "#6c63ff")],
     #       foreground=[("active", "#ffffff")]
    #    )

        # --- Target Language Selection ---
     #   ttk.Label(root, text="🎯 Target Language:").grid(row=0, column=0, sticky="w", padx=12, pady=(15, 5))
#
     #   self.languages = ["Python", "JavaScript", "C++", "Java", "Go"]
     #   self.target_lang = tk.StringVar(value="JavaScript")

      #  self.lang_frame = tk.Frame(root, bg="")
      #  self.lang_frame.grid(row=1, column=0, sticky="w", padx=12, pady=5)
     #   for lang in self.languages:
     #       ttk.Radiobutton(self.lang_frame, text=lang, value=lang, variable=self.target_lang).pack(side="left", padx=5)

        # --- Input Code Section ---
       # ttk.Label(root, text="🧩 Input Code:").grid(row=2, column=0, sticky="w", padx=12, pady=(10, 2))
       # self.input_text = scrolledtext.ScrolledText(
      #      root, bg="#1e1e1e", fg="#dcdcdc",
      #      insertbackground="#ffffff", font=("Consolas", 12),
       #     wrap=tk.WORD
      #  )
      #  self.input_text.insert("1.0", "# Paste your code here...")
     #   self.input_text.grid(row=3, column=0, sticky="nsew", padx=12, pady=5)

        # --- Buttons ---
       # self.button_frame = tk.Frame(root, bg="#121212")
       # self.button_frame.grid(row=4, column=0, sticky="ew", padx=12, pady=10)
      #  self.button_frame.columnconfigure((0, 1, 2, 3), weight=1)

    #    ttk.Button(self.button_frame, text="🪄 Convert", command=lambda: self.call_backend("convert")).grid(row=0, column=0, sticky="ew", padx=5)
     #   ttk.Button(self.button_frame, text="🩺 Fix", command=lambda: self.call_backend("fix")).grid(row=0, column=1, sticky="ew", padx=5)
    #    ttk.Button(self.button_frame, text="▶️ Run", command=lambda: self.call_backend("run")).grid(row=0, column=2, sticky="ew", padx=5)
   #     ttk.Button(self.button_frame, text="🎨 Change BG", command=self.change_bg_color).grid(row=0, column=3, sticky="ew", padx=5)

        # --- Status Label ---
     #   self.status_label = ttk.Label(self.button_frame, text="", foreground="#ccc", background="#121212", font=("Segoe UI", 10))
     #   self.status_label.grid(row=1, column=0, columnspan=4, pady=(6, 0))

        # --- Output Code Section ---
     #   ttk.Label(root, text="📤 Output:").grid(row=5, column=0, sticky="w", padx=12, pady=(10, 2))
     #   self.output_text = scrolledtext.ScrolledText(
    #        root, bg="#1e1e1e", fg="#dcdcdc",
     #       font=("Consolas", 12), wrap=tk.WORD
      #  )
      #  self.output_text.insert("1.0", "# Output will appear here...")
     #   self.output_text.grid(row=6, column=0, sticky="nsew", padx=12, pady=5)

        # --- Responsive Layout ---
     #   for i in [3, 6]:
     #       root.rowconfigure(i, weight=1)
       # root.columnconfigure(0, weight=1)

    # --- Function to Change Background Color ---
  #  def change_bg_color(self):
   #     from tkinter import colorchooser
    #    color = colorchooser.askcolor(title="Choose Background Color")[1]
     #   if color:
      #      self.root.configure(bg=color)
       #     self.lang_frame.configure(bg=color)
        #    self.button_frame.configure(bg=color)
        #    self.input_text.configure(bg=color)
         #   self.output_text.configure(bg=color)"""
"""class CodeWizardApp:
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

        # --- Header / Title Frame ---
        self.header_frame = tk.Frame(root, bg="#121212")
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=12, pady=(10, 0))
        ttk.Label(self.header_frame, text="🎯 Target Language:").pack(side="left", padx=(0, 8))

        self.languages = ["Python", "JavaScript", "C++", "Java", "Go"]
        self.target_lang = tk.StringVar(value="JavaScript")
        for lang in self.languages:
            ttk.Radiobutton(self.header_frame, text=lang, value=lang, variable=self.target_lang).pack(side="left", padx=5)

        # --- Input Code Section ---
        ttk.Label(root, text="🧩 Input Code:").grid(row=1, column=0, sticky="w", padx=12, pady=(10, 2))
        self.input_text = scrolledtext.ScrolledText(
            root, bg="#1e1e1e", fg="#dcdcdc",
            insertbackground="#ffffff", font=("Consolas", 12),
            wrap=tk.WORD
        )
        self.input_text.insert("1.0", "# Paste your code here...")
        self.input_text.grid(row=2, column=0, sticky="nsew", padx=12, pady=5)

        # --- Buttons (Middle Section) ---
        self.button_frame = tk.Frame(root, bg="#121212")
        self.button_frame.grid(row=3, column=0, sticky="ew", padx=12, pady=10)
        self.button_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)

        ttk.Button(self.button_frame, text="🪄 Convert", command=lambda: self.call_backend("convert")).grid(row=0, column=0, sticky="ew", padx=5)
        ttk.Button(self.button_frame, text="🩺 Fix", command=lambda: self.call_backend("fix")).grid(row=0, column=1, sticky="ew", padx=5)
        ttk.Button(self.button_frame, text="▶️ Run", command=lambda: self.call_backend("run")).grid(row=0, column=2, sticky="ew", padx=5)
        ttk.Button(self.button_frame, text="🎨 Change BG", command=self.change_bg_color).grid(row=0, column=3, sticky="ew", padx=5)
        ttk.Button(self.button_frame, text="🧱 Change Header/Footer", command=self.change_header_footer_color).grid(row=0, column=4, sticky="ew", padx=5)

        self.status_label = ttk.Label(self.button_frame, text="", foreground="#ccc", background="#121212", font=("Segoe UI", 10))
        self.status_label.grid(row=1, column=0, columnspan=5, pady=(6, 0))

        # --- Output Section (Footer) ---
        self.footer_frame = tk.Frame(root, bg="#121212")
        self.footer_frame.grid(row=4, column=0, sticky="ew", padx=12, pady=(10, 0))
        ttk.Label(self.footer_frame, text="📤 Output:").pack(side="left", padx=(0, 8))

        self.output_text = scrolledtext.ScrolledText(
            root, bg="#1e1e1e", fg="#dcdcdc",
            font=("Consolas", 12), wrap=tk.WORD
        )
        self.output_text.insert("1.0", "# Output will appear here...")
        self.output_text.grid(row=5, column=0, sticky="nsew", padx=12, pady=5)

        # --- Responsive Layout ---
        for i in [2, 5]:
            root.rowconfigure(i, weight=1)
        root.columnconfigure(0, weight=1)

    # --- Function to Change Background Color (full area) ---
    def change_bg_color(self):
        from tkinter import colorchooser
        color = colorchooser.askcolor(title="Choose Background Color")[1]
        if color:
            self.root.configure(bg=color)
            self.header_frame.configure(bg=color)
            self.button_frame.configure(bg=color)
            self.footer_frame.configure(bg=color)
            self.input_text.configure(bg=color)
            self.output_text.configure(bg=color)

            # Update ttk label backgrounds dynamically
            for widget in self.root.winfo_children():
                if isinstance(widget, ttk.Label):
                    widget.configure(background=color)
            for widget in self.button_frame.winfo_children():
                if isinstance(widget, ttk.Label):
                    widget.configure(background=color)

    # --- Function to Change Header/Footer Colors Independently ---
    def change_header_footer_color(self):
        from tkinter import colorchooser
        color = colorchooser.askcolor(title="Choose Header/Footer Color")[1]
        if color:
            self.header_frame.configure(bg=color)
            self.footer_frame.configure(bg=color)
            for frame in [self.header_frame, self.footer_frame]:
                for widget in frame.winfo_children():
                    if isinstance(widget, ttk.Label):
                        widget.configure(background=color)



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

"""class CodeWizardApp:
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
        root.columnconfigure(0, weight=1)"""
"""class CodeWizardApp:
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

        self.lang_frame = tk.Frame(root, bg="")
        self.lang_frame.grid(row=1, column=0, sticky="w", padx=12, pady=5)
        for lang in self.languages:
            ttk.Radiobutton(self.lang_frame, text=lang, value=lang, variable=self.target_lang).pack(side="left", padx=5)

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
        self.button_frame = tk.Frame(root, bg="#121212")
        self.button_frame.grid(row=4, column=0, sticky="ew", padx=12, pady=10)
        self.button_frame.columnconfigure((0, 1, 2, 3), weight=1)

        ttk.Button(self.button_frame, text="🪄 Convert", command=lambda: self.call_backend("convert")).grid(row=0, column=0, sticky="ew", padx=5)
        ttk.Button(self.button_frame, text="🩺 Fix", command=lambda: self.call_backend("fix")).grid(row=0, column=1, sticky="ew", padx=5)
        ttk.Button(self.button_frame, text="▶️ Run", command=lambda: self.call_backend("run")).grid(row=0, column=2, sticky="ew", padx=5)
        ttk.Button(self.button_frame, text="🎨 Change BG", command=self.change_bg_color).grid(row=0, column=3, sticky="ew", padx=5)

        # --- Status Label ---
        self.status_label = ttk.Label(self.button_frame, text="", foreground="#ccc", background="#121212", font=("Segoe UI", 10))
        self.status_label.grid(row=1, column=0, columnspan=4, pady=(6, 0))

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

    # --- Function to Change Background Color ---
    def change_bg_color(self):
        from tkinter import colorchooser
        color = colorchooser.askcolor(title="Choose Background Color")[1]
        if color:
            self.root.configure(bg=color)
            self.lang_frame.configure(bg=color)
            self.button_frame.configure(bg=color)
            self.input_text.configure(bg=color)
            self.output_text.configure(bg=color)""" """
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

        # --- Header / Title Frame ---
        self.header_frame = tk.Frame(root, bg="#121212")
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=12, pady=(10, 0))
        ttk.Label(self.header_frame, text="🎯 Target Language:").pack(side="left", padx=(0, 8))

        self.languages = ["Python", "JavaScript", "C++", "Java", "Go"]
        self.target_lang = tk.StringVar(value="JavaScript")
        for lang in self.languages:
            ttk.Radiobutton(self.header_frame, text=lang, value=lang, variable=self.target_lang).pack(side="left", padx=5)

        # --- Input Code Section ---
        ttk.Label(root, text="🧩 Input Code:").grid(row=1, column=0, sticky="w", padx=12, pady=(10, 2))
        self.input_text = scrolledtext.ScrolledText(
            root, bg="#1e1e1e", fg="#dcdcdc",
            insertbackground="#ffffff", font=("Consolas", 12),
            wrap=tk.WORD
        )
        self.input_text.insert("1.0", "# Paste your code here...")
        self.input_text.grid(row=2, column=0, sticky="nsew", padx=12, pady=5)

        # --- Buttons (Middle Section) ---
        self.button_frame = tk.Frame(root, bg="#121212")
        self.button_frame.grid(row=3, column=0, sticky="ew", padx=12, pady=10)
        self.button_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)

        ttk.Button(self.button_frame, text="🪄 Convert", command=lambda: self.call_backend("convert")).grid(row=0, column=0, sticky="ew", padx=5)
        ttk.Button(self.button_frame, text="🩺 Fix", command=lambda: self.call_backend("fix")).grid(row=0, column=1, sticky="ew", padx=5)
        ttk.Button(self.button_frame, text="▶️ Run", command=lambda: self.call_backend("run")).grid(row=0, column=2, sticky="ew", padx=5)
        ttk.Button(self.button_frame, text="🎨 Change BG", command=self.change_bg_color).grid(row=0, column=3, sticky="ew", padx=5)
        ttk.Button(self.button_frame, text="🧱 Change Header/Footer", command=self.change_header_footer_color).grid(row=0, column=4, sticky="ew", padx=5)

        self.status_label = ttk.Label(self.button_frame, text="", foreground="#ccc", background="#121212", font=("Segoe UI", 10))
        self.status_label.grid(row=1, column=0, columnspan=5, pady=(6, 0))

        # --- Output Section (Footer) ---
        self.footer_frame = tk.Frame(root, bg="#121212")
        self.footer_frame.grid(row=4, column=0, sticky="ew", padx=12, pady=(10, 0))
        ttk.Label(self.footer_frame, text="📤 Output:").pack(side="left", padx=(0, 8))

        self.output_text = scrolledtext.ScrolledText(
            root, bg="#1e1e1e", fg="#dcdcdc",
            font=("Consolas", 12), wrap=tk.WORD
        )
        self.output_text.insert("1.0", "# Output will appear here...")
        self.output_text.grid(row=5, column=0, sticky="nsew", padx=12, pady=5)

        # --- Responsive Layout ---
        for i in [2, 5]:
            root.rowconfigure(i, weight=1)
        root.columnconfigure(0, weight=1)

    # --- Function to Change Background Color (full area) ---
    def change_bg_color(self):
        from tkinter import colorchooser
        color = colorchooser.askcolor(title="Choose Background Color")[1]
        if color:
            self.root.configure(bg=color)
            self.header_frame.configure(bg=color)
            self.button_frame.configure(bg=color)
            self.footer_frame.configure(bg=color)
            self.input_text.configure(bg=color)
            self.output_text.configure(bg=color)

            # Update ttk label backgrounds dynamically
            for widget in self.root.winfo_children():
                if isinstance(widget, ttk.Label):
                    widget.configure(background=color)
            for widget in self.button_frame.winfo_children():
                if isinstance(widget, ttk.Label):
                    widget.configure(background=color)

    # --- Function to Change Header/Footer Colors Independently ---
    def change_header_footer_color(self):
        from tkinter import colorchooser
        color = colorchooser.askcolor(title="Choose Header/Footer Color")[1]
        if color:
            self.header_frame.configure(bg=color)
            self.footer_frame.configure(bg=color)
            for frame in [self.header_frame, self.footer_frame]:
                for widget in frame.winfo_children():
                    if isinstance(widget, ttk.Label):
                        widget.configure(background=color)



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
    root.mainloop() """

import streamlit as st
import subprocess
import tempfile
import os
import io
import contextlib
from openai import OpenAI
from dotenv import load_dotenv
import re

# -------------------- Load Environment Variables --------------------
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -------------------- Streamlit Page Config --------------------
st.set_page_config(page_title="✨ Codemorph ", page_icon="🪄", layout="wide")

# -------------------- Sidebar UI --------------------
with st.sidebar:
    st.title("⚙️ Settings")

    st.markdown("### 🎯 Target Language")
    target_lang = st.selectbox(
        "Select output language",
        ["Python", "C", "C++", "Java", "JavaScript"],
        index=0,
    )

    st.markdown("### 🎨 Background Color")
    bg_color = st.color_picker("Choose background", "#E4E7EF")

    st.markdown("### 🧱 Header/Footer Color")
    header_color = st.color_picker("Choose header/footer", "#dce3f5")

# -------------------- Custom CSS --------------------
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {bg_color};
        }}
        .main-title {{
            background-color: {header_color};
            padding: 20px;
            border-radius: 20px;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #222;
        }}
        .footer {{
            text-align: center;
            color: gray;
            margin-top: 40px;
        }}
        textarea, .stTextArea textarea {{
            background-color: white !important;
            color: black !important;
            border-radius: 10px !important;
            border: 1px solid #ccc !important;
            font-size: 15px !important;
        }}
        .run-output {{
            background: #000;
            color: #00ff88;
            font-family: monospace;
            padding: 10px;
            border-radius: 10px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------- Main Title --------------------
st.markdown('<div class="main-title">🪄 Codemorph </div>', unsafe_allow_html=True)
st.write("")

# -------------------- Input Code Section --------------------
st.subheader("🧩 Input Code")
code_input = st.text_area("Paste your code here 👇", height=250, placeholder="Type or paste your code...")

# Input for runtime data
user_input_data = st.text_area("📥 Program Input (if any)", height=100, placeholder="Enter input for your code (optional)")

# -------------------- Action Buttons --------------------
col1, col2, col3, col4 = st.columns(4)
convert = col1.button("🔁 Convert")
fix = col2.button("🩹 Fix")
analyze = col3.button("💡 Analyze")
run_local = col4.button("🚀 Run Code")

# -------------------- Helper: Clean Emojis --------------------
def clean_text(text):
    """Removes emojis/unicode symbols for safe console printing."""
    return re.sub(r"[^\x00-\x7F]+", "", text)

# -------------------- Helper: OpenAI Integration --------------------
def ask_openai(task: str, code_text: str, lang: str):
    try:
        detect_prompt = f"Detect the programming language of the following code:\n\n{code_text}"
        detect_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": detect_prompt}],
        )
        detected_lang = detect_response.choices[0].message.content.strip()

        prompt = f"""
        You are a professional code assistant.
        The user wants to {task} this code.
        Detected input language: {detected_lang}.
        Target language: {lang}.
        Code:
        {code_text}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert code engineer and teacher."},
                {"role": "user", "content": prompt},
            ],
        )
        result = response.choices[0].message.content
        return clean_text(result)
    except Exception as e:
        return f"❌ Error: {e}"

# -------------------- Safe Runner for Multiple Languages --------------------
def run_code(language, code, input_data=""):
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            env = os.environ.copy()
            env["PYTHONIOENCODING"] = "utf-8"
            env["JAVA_TOOL_OPTIONS"] = "-Dfile.encoding=UTF-8"
            env["NODE_OPTIONS"] = "--input-type=module"

            # Write file safely
            def write_file(name, content):
                path = os.path.join(tmpdir, name)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                return path

            if language == "Python":
                file_path = write_file("main.py", code)
                result = subprocess.run(
                    ["python", file_path],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=10,
                    env=env,
                    encoding="utf-8",
                    errors="ignore",
                )

            elif language == "C":
                file_path = write_file("main.c", code)
                exe_path = os.path.join(tmpdir, "main.exe")
                subprocess.run(["gcc", file_path, "-o", exe_path], capture_output=True, text=True, env=env)
                result = subprocess.run(
                    [exe_path],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=10,
                    env=env,
                    encoding="utf-8",
                    errors="ignore",
                )

            elif language == "C++":
                file_path = write_file("main.cpp", code)
                exe_path = os.path.join(tmpdir, "main.exe")
                subprocess.run(["g++", file_path, "-o", exe_path], capture_output=True, text=True, env=env)
                result = subprocess.run(
                    [exe_path],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=10,
                    env=env,
                    encoding="utf-8",
                    errors="ignore",
                )

            elif language == "Java":
                file_path = write_file("Main.java", code)
                subprocess.run(["javac", file_path], capture_output=True, text=True, env=env)
                result = subprocess.run(
                    ["java", "-cp", tmpdir, "Main"],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=10,
                    env=env,
                    encoding="utf-8",
                    errors="ignore",
                )

            elif language == "JavaScript":
                file_path = write_file("main.js", code)
                result = subprocess.run(
                    ["node", file_path],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=10,
                    env=env,
                    encoding="utf-8",
                    errors="ignore",
                )

            else:
                return "⚠️ Unsupported language."

            output = result.stdout or result.stderr
            return clean_text(output.strip()) if output else "(No output)"

    except subprocess.TimeoutExpired:
        return "⏱️ Execution timed out."
    except Exception as e:
        return f"❌ Error while running code: {e}"

# -------------------- Actions --------------------
if convert and code_input.strip():
    with st.spinner("🔄 Converting your code..."):
        result = ask_openai("convert", code_input, target_lang)
        st.subheader("✅ Converted Code")
        st.code(result, language=target_lang.lower())

elif fix and code_input.strip():
    with st.spinner("🩹 Fixing your code..."):
        result = ask_openai("fix", code_input, target_lang)
        st.subheader("✅ Fixed Code")
        st.code(result, language=target_lang.lower())

elif analyze and code_input.strip():
    with st.spinner("🧠 Analyzing your code..."):
        result = ask_openai("explain", code_input, target_lang)
        st.subheader("🧩 Code Analysis")
        st.write(result)
elif run_local and code_input.strip():
    with st.spinner("🚀 Running your code safely..."):
        # Detect language from code pattern (basic heuristic)
        code_snippet = code_input.strip()

        # Auto-detect actual code language from syntax
        if code_snippet.startswith("import javax") or "public class" in code_snippet:
            run_lang = "Java"
        elif "#include" in code_snippet and "iostream" in code_snippet:
            run_lang = "C++"
        elif "#include" in code_snippet:
            run_lang = "C"
        elif "console.log" in code_snippet:
            run_lang = "JavaScript"
        else:
            run_lang = "Python"

        output = run_code(run_lang, code_input, user_input_data)
        st.subheader(f"🖥️ Output Console ({run_lang})")
        st.markdown(f"<div class='run-output'>{output}</div>", unsafe_allow_html=True)


