import customtkinter as ctk
from calculator import solve

#! DO NOT FORGET to finish the project and deploy it so that it can be seen 
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ScientificCalculator(ctk.CTk):
    ERROR_TEXTS = {
        "Syntax Error",
        "Math Error",
        "Error",
        "SyntaxErr",
        "SyntaxErr: close bracket",
        "if you know you know",
    }

    FRONTEND_TOKENS = [
        "sqrt(",
        "sin(",
        "cos(",
        "tan(",
        "log(",
        "ln(",
        "^2",
    ]

    KEYBOARD_TOKENS = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        ".": ".",
        "+": "+",
        "-": "-",
        "*": "*",
        "/": "/",
        "(": "(",
        ")": ")",
        "^": "^",
        "×": "*",
        "÷": "/",
    }

    BUTTON_ROWS = [
        [
            {"label": "2nd", "action": "second", "style": "disabled"},
            {"label": "DEG", "action": "mode", "style": "mode"},
            {"label": "sin", "action": "sin(", "style": "scientific"},
            {"label": "cos", "action": "cos(", "style": "scientific"},
            {"label": "tan", "action": "tan(", "style": "scientific"},
            {"label": "√", "action": "sqrt(", "style": "scientific"},
        ],
        [
            {"label": "x²", "action": "^2", "style": "scientific"},
            {"label": "xʸ", "action": "^", "style": "scientific"},
            {"label": "log", "action": "log(", "style": "scientific"},
            {"label": "ln", "action": "ln(", "style": "scientific"},
            {"label": "(", "action": "(", "style": "scientific"},
            {"label": ")", "action": ")", "style": "scientific"},
        ],
        [
            {"label": "π", "action": "π", "style": "scientific"},
            {"label": "e", "action": "e", "style": "scientific"},
            {"label": "AC", "action": "clear", "style": "control"},
            {"label": "DEL", "action": "delete", "style": "control"},
            {"label": "÷", "action": "/", "style": "operator"},
            {"label": "×", "action": "*", "style": "operator"},
        ],
        [
            {"label": "7", "action": "7", "style": "number", "span": 2},
            {"label": "8", "action": "8", "style": "number", "span": 2},
            {"label": "9", "action": "9", "style": "number"},
            {"label": "−", "action": "-", "style": "operator"},
        ],
        [
            {"label": "4", "action": "4", "style": "number", "span": 2},
            {"label": "5", "action": "5", "style": "number", "span": 2},
            {"label": "6", "action": "6", "style": "number"},
            {"label": "+", "action": "+", "style": "operator"},
        ],
        [
            {"label": "1", "action": "1", "style": "number", "span": 2},
            {"label": "2", "action": "2", "style": "number", "span": 2},
            {"label": "3", "action": "3", "style": "number"},
            {"label": "=", "action": "equals", "style": "equals", "rowspan": 2},
        ],
        [
            {"label": "0", "action": "0", "style": "number", "span": 3},
            {"label": ".", "action": ".", "style": "number", "span": 2},
        ],
    ]

    COLORS = {
        "background": "#0b0f13",
        "panel": "#0d131a",
        "display": "#111a23",
        "display_border": "#1d2f3f",
        "preview": "#10283a",
        "text": "#e9eef6",
        "muted": "#7f8b9b",
        "scientific": "#2d3848",
        "scientific_hover": "#38465a",
        "number": "#282828",
        "number_hover": "#343434",
        "operator": "#94c4f4",
        "operator_hover": "#a7d0f7",
        "operator_text": "#1e3f5e",
        "control": "#444442",
        "control_hover": "#555451",
        "equals": "#8fc4f7",
        "equals_hover": "#a4d1fb",
        "disabled": "#202832",
    }

    def __init__(self):
        super().__init__()
        self.angle_mode = "deg"
        self.internal_expression = ""
        self.display_expression = ""
        self.displayed_result = ""
        self.error_state = False
        self.history = []

        self.expression_var = ctk.StringVar(value="")
        self.result_var = ctk.StringVar(value="0")
        self.history_var = ctk.StringVar(value="")
        self.history_labels = []

        self.title("Modern Scientific Calculator")
        self.geometry("1180x740")
        self.minsize(900, 620)
        self.resizable(True, True)
        self.configure(fg_color=self.COLORS["background"])

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)

        self.create_header()
        self.create_display_area()
        self.create_keypad()
        self.refresh_display()
        self.bind_all("<Key>", self.handle_keyboard_input)

    def create_header(self):
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, padx=20, pady=(14, 8), sticky="ew")
        header.grid_columnconfigure(0, weight=0)
        header.grid_columnconfigure(1, weight=1)
        header.grid_columnconfigure(2, weight=0)

        self.info_button = self.create_icon_button(header, "i", lambda: None)
        self.info_button.grid(row=0, column=0, sticky="w")

        title = ctk.CTkLabel(
            header,
            text="Modern Scientific Calculator",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color=self.COLORS["text"],
        )
        title.grid(row=0, column=1, sticky="ew")

        actions = ctk.CTkFrame(header, fg_color="transparent")
        actions.grid(row=0, column=2, sticky="e")
        self.clear_history_button = self.create_icon_button(actions, "↺", self.clear_history)
        self.clear_history_button.grid(row=0, column=0, padx=(0, 8))
        self.copy_button = self.create_icon_button(actions, "⧉", self.copy_result)
        self.copy_button.grid(row=0, column=1)

    def create_icon_button(self, parent, text, command):
        return ctk.CTkButton(
            parent,
            text=text,
            width=34,
            height=34,
            corner_radius=17,
            fg_color="#0f141a",
            hover_color="#19212a",
            text_color="#c6ced8",
            font=ctk.CTkFont(family="Segoe UI", size=17, weight="bold"),
            command=command,
        )

    def create_display_area(self):
        display_area = ctk.CTkFrame(self, fg_color="transparent")
        display_area.grid(row=1, column=0, padx=20, pady=(0, 22), sticky="ew")
        display_area.grid_columnconfigure(0, weight=1)
        display_area.grid_rowconfigure(0, weight=0)
        display_area.grid_rowconfigure(1, weight=0)
        display_area.grid_rowconfigure(2, weight=0)

        history_panel = ctk.CTkFrame(display_area, fg_color="transparent")
        history_panel.grid(row=0, column=0, sticky="ew")
        history_panel.grid_columnconfigure(0, weight=1)

        for row in range(3):
            history_panel.grid_rowconfigure(row, weight=1)
            label = ctk.CTkLabel(
                history_panel,
                text="",
                anchor="e",
                justify="right",
                height=18,
                font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
                text_color=self.COLORS["muted"],
            )
            label.grid(row=row, column=0, sticky="ew")
            self.history_labels.append(label)

        self.history_label = ctk.CTkLabel(
            display_area,
            textvariable=self.history_var,
            anchor="e",
            justify="right",
            height=54,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color=self.COLORS["muted"],
        )
        self.history_label.grid_forget()

        preview = ctk.CTkFrame(display_area, fg_color=self.COLORS["preview"], corner_radius=13)
        preview.grid(row=1, column=0, pady=(4, 8), sticky="ew")
        preview.grid_columnconfigure(0, weight=1)

        self.expression_label = ctk.CTkLabel(
            preview,
            textvariable=self.expression_var,
            anchor="e",
            justify="right",
            height=34,
            padx=14,
            font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold"),
            text_color="#d2dce9",
        )
        self.expression_label.grid(row=0, column=0, sticky="ew")

        display = ctk.CTkFrame(
            display_area,
            fg_color=self.COLORS["display"],
            corner_radius=16,
            border_width=1,
            border_color=self.COLORS["display_border"],
        )
        display.grid(row=2, column=0, sticky="ew")
        display.grid_columnconfigure(0, weight=1)

        self.result_label = ctk.CTkLabel(
            display,
            textvariable=self.result_var,
            anchor="e",
            justify="right",
            height=96,
            padx=20,
            font=ctk.CTkFont(family="Segoe UI", size=40),
            text_color="#edf3fb",
        )
        self.result_label.grid(row=0, column=0, padx=2, pady=2, sticky="ew")

    def create_keypad(self):
        keypad = ctk.CTkFrame(self, fg_color="transparent")
        keypad.grid(row=2, column=0, padx=20, pady=(0, 16), sticky="nsew")

        for column in range(6):
            keypad.grid_columnconfigure(column, weight=1, uniform="button_columns")
        for row in range(7):
            keypad.grid_rowconfigure(row, weight=1, uniform="button_rows")

        for row_index, row in enumerate(self.BUTTON_ROWS):
            column_index = 0
            for config in row:
                span = config.get("span", 1)
                rowspan = config.get("rowspan", 1)
                self.add_button(
                    keypad,
                    config["label"],
                    config["action"],
                    config["style"],
                    row_index,
                    column_index,
                    span,
                    rowspan,
                )
                column_index += span

    def add_button(self, parent, label, action, style, row, column, colspan=1, rowspan=1):
        colors = self.get_button_colors(style)
        button = ctk.CTkButton(
            parent,
            text=label,
            height=40,
            corner_radius=13,
            fg_color=colors["fg"],
            hover_color=colors["hover"],
            text_color=colors["text"],
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            command=lambda: self.handle_button_action(action),
            state="disabled" if style == "disabled" else "normal",
        )
        button.grid(
            row=row,
            column=column,
            columnspan=colspan,
            rowspan=rowspan,
            padx=4,
            pady=4,
            sticky="nsew",
        )

        if action == "mode":
            self.mode_button = button

        return button

    def get_button_colors(self, style):
        if style == "number":
            return {"fg": self.COLORS["number"], "hover": self.COLORS["number_hover"], "text": "#dce2ea"}
        if style == "operator":
            return {"fg": self.COLORS["operator"], "hover": self.COLORS["operator_hover"], "text": self.COLORS["operator_text"]}
        if style == "control":
            return {"fg": self.COLORS["control"], "hover": self.COLORS["control_hover"], "text": "#f0f2f5"}
        if style == "equals":
            return {"fg": self.COLORS["equals"], "hover": self.COLORS["equals_hover"], "text": self.COLORS["operator_text"]}
        if style == "mode":
            return {"fg": "#2f4158", "hover": "#3b506b", "text": "#b6d5fb"}
        if style == "disabled":
            return {"fg": self.COLORS["disabled"], "hover": self.COLORS["disabled"], "text": "#86a9ce"}
        return {"fg": self.COLORS["scientific"], "hover": self.COLORS["scientific_hover"], "text": "#a9cdf6"}

    def handle_button_action(self, action):
        if action == "clear":
            self.clear_all()
        elif action == "delete":
            self.delete_token()
        elif action == "equals":
            self.calculate_result()
        elif action == "mode":
            self.toggle_angle_mode()
        elif action != "second":
            self.append_token(action)

    def append_token(self, token):
        if self.error_state:
            self.internal_expression = ""
            self.display_expression = ""
            self.displayed_result = ""
            self.error_state = False

        self.internal_expression += token
        self.display_expression = self.to_display_expression(self.internal_expression)
        self.displayed_result = self.display_expression
        self.refresh_display()

    def delete_token(self):
        if self.error_state or self.is_error_displayed():
            self.internal_expression = ""
            self.display_expression = ""
            self.displayed_result = ""
            self.error_state = False
            self.refresh_display()
            return

        if not self.internal_expression:
            self.display_expression = ""
            self.displayed_result = ""
            self.refresh_display()
            return

        for token in self.FRONTEND_TOKENS:
            if self.internal_expression.endswith(token):
                self.internal_expression = self.internal_expression[:-len(token)]
                break
        else:
            self.internal_expression = self.internal_expression[:-1]

        self.display_expression = self.to_display_expression(self.internal_expression)
        self.displayed_result = self.display_expression
        self.refresh_display()

    def clear_all(self):
        self.internal_expression = ""
        self.display_expression = ""
        self.displayed_result = ""
        self.error_state = False
        self.refresh_display()

    def calculate_result(self):
        expression = self.internal_expression
        if not expression or self.error_state:
            return

        result = solve(expression, self.angle_mode)
        self.displayed_result = str(result)
        self.error_state = self.is_error_value(self.displayed_result)
        self.add_history(expression, self.displayed_result)
        self.internal_expression = "" if self.error_state else self.displayed_result
        self.display_expression = "" if self.error_state else self.to_display_expression(self.internal_expression)
        self.refresh_display()

    def toggle_angle_mode(self):
        self.angle_mode = "rad" if self.angle_mode == "deg" else "deg"
        self.mode_button.configure(text=self.angle_mode.upper())
        self.update_mode_button_style()

    def update_mode_button_style(self):
        if self.angle_mode == "deg":
            self.mode_button.configure(fg_color="#2f4158", hover_color="#3b506b", text_color="#b6d5fb")
        else:
            self.mode_button.configure(fg_color="#4f4630", hover_color="#65583b", text_color="#f0d79a")

    def add_history(self, expression, result):
        if self.is_error_value(result):
            return

        self.history.append(f"{self.to_display_expression(expression)} = {result}")
        self.history = self.history[-3:]
        self.refresh_history()

    def refresh_history(self):
        visible_items = self.history[-3:]
        lines = []
        for index, item in enumerate(visible_items):
            lines.append(item)
        self.history_var.set("\n".join(lines))

        if hasattr(self, "history_labels"):
            padded_items = [""] * (3 - len(visible_items)) + visible_items
            newest_index = len(padded_items) - 1
            for index, label in enumerate(self.history_labels):
                label.configure(
                    text=padded_items[index],
                    text_color="#d6deea" if index == newest_index and padded_items[index] else self.COLORS["muted"],
                )

    def clear_history(self):
        self.history.clear()
        self.refresh_history()

    def copy_result(self):
        value = self.displayed_result or self.display_expression
        if value:
            self.clipboard_clear()
            self.clipboard_append(value)

    def refresh_display(self):
        self.display_expression = self.to_display_expression(self.internal_expression)
        preview_text = self.display_expression
        if self.error_state:
            preview_text = ""

        result_text = self.displayed_result or "0"
        self.expression_var.set(preview_text)
        self.result_var.set(result_text)
        self.refresh_history()

    def to_display_expression(self, expression):
        return str(expression).replace("*", "×").replace("/", "÷")

    def is_error_displayed(self):
        return self.is_error_value(self.displayed_result)

    def is_error_value(self, value):
        text = str(value)
        return text in self.ERROR_TEXTS or text.startswith("SyntaxErr")

    def handle_keyboard_input(self, event):
        key = event.keysym
        char = event.char

        if key in ("Return", "KP_Enter"):
            self.calculate_result()
            return "break"

        if key == "BackSpace":
            self.delete_token()
            return "break"

        if key == "Escape":
            self.clear_all()
            return "break"

        if char in self.KEYBOARD_TOKENS:
            self.append_token(self.KEYBOARD_TOKENS[char])
            return "break"

        return "break"


if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
