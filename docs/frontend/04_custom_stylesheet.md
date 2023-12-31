### **Custom Stylesheets in Nextpy: A Guide with Engaging Examples**

**Incorporating External Stylesheets**

- Nextpy opens the door to a world of styling by allowing you to integrate external CSS files.
- Simply provide the URLs of these stylesheets when you conjure your app.

**Example: Enlivening with Animate.css**

```python

app = xt.App(
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    ],
)

```

- Imagine bringing your app to life with the flair of animations from the Animate.css library.

**Employing Local Stylesheets**

- Nextpy also empowers you to weave your own styling spells with custom CSS files nestled in the **`assets/`** directory.

**Example: Crafting Your Style**

```python

app = xt.App(
    stylesheets=["styles.css"],  # A treasure map to your own style in assets/
)

```

- **`styles.css`** acts as your personal stylist, housed within your app's assets.

### **Infusing Personality with Custom Fonts in Nextpy**

**Harnessing External Fonts**

- Nextpy's custom stylesheet feature lets you add a touch of personality with external fonts.
- You can set the **`font_family`** prop to flaunt these fonts in your app.

**Example: Showcasing Google Fonts**

```python

xt.text(
    "Explore IBM Plex Mono",
    font_family="IBM Plex Mono",
    font_size="1.5em",
)

```

- Here, the chic IBM Plex Mono font from Google Fonts adds a sophisticated touch to your text.

**Utilizing Local Fonts**

- Nextpy also supports fonts hosted on your own server, allowing for a more personalized touch.

**Steps for Adding a Local Font:**

1. **Placing the Font File:**
    - Add your **`MyFont.otf`** font into the **`assets/fonts`** treasure trove.
2. **Weaving a CSS Spell for Your Font:**
    
    ```css
    
    @font-face {
        font-family: MyFont;
        src: url("MyFont.otf") format("opentype");
    }
    @font-face {
        font-family: MyFont;
        font-weight: bold;
        src: url("MyFont.otf") format("opentype");
    }
    
    ```
    
3. **Linking the Stylesheet to Your App:**
    
    ```python
    
    app = xt.App(
        stylesheets=["fonts/myfont.css"],  # The secret path to your font's style
    )
    
    ```
    
4. **Flaunting the Font in Your Components:**
    - **`MyFont`** now stands ready to grace any component with its unique style.

**Example: Parading the Local Font**

```python

xt.text("Greetings in MyFont", font_family="MyFont")

```

- Envision **`MyFont`** giving a distinctive character to your text, much like wearing a custom-tailored outfit.
