# 📊 Slides Structure - Multi-Armed Bandit

This document explains the improved slide architecture for this algorithm.

## 🏗️ Architecture Overview

### **Modular Slide System**
Each slide is now a **separate HTML file** for better organization and maintainability.

```
algorithms/multi-armed-bandit/
├── index.html              # Main page (loads slides dynamically)
├── algorithm.css           # Styling
├── mab_demo.py            # Python implementation
├── slides/
│   ├── slide1.html        # Problem Formulation
│   ├── slide2.html        # ε-Greedy Strategy
│   ├── slide3.html        # UCB Algorithm
│   └── slide4.html        # Interactive Demo
└── SLIDES_README.md       # This file
```

---

## ✨ Key Features

### 1. **Beautiful Math Rendering with KaTeX**

Instead of plain text:
```
L_T = T · E[R | a*] - Σ E[R_t]
```

You now get beautiful LaTeX-rendered formulas:
```latex
L_T = T \cdot \mathbb{E}[R | a^*] - \sum_{t=1}^{T} \mathbb{E}[R_t]
```

**Usage in slides:**
```html
<!-- Inline math -->
<span class="math">Q_t(a) = \mathbb{E}[R_t | A_t = a]</span>

<!-- Display (centered) math -->
<div class="math-display">
    A_t = \arg\max_a \left[ Q_t(a) + c \sqrt{\frac{\ln t}{N_t(a)}} \right]
</div>
```

### 2. **Dynamic Slide Loading**

The main `index.html` automatically:
- Fetches all slide files via JavaScript `fetch()`
- Renders math formulas with KaTeX
- Applies syntax highlighting with Prism.js
- Handles navigation and keyboard shortcuts

### 3. **Independent Slide Files**

**Benefits:**
- ✅ **Easy editing**: Modify one slide without touching others
- ✅ **Version control**: See changes per slide in Git diff
- ✅ **Reusability**: Copy slides to other algorithms
- ✅ **Collaboration**: Multiple people can edit different slides
- ✅ **Testing**: Debug individual slides separately

---

## 📝 Creating a New Slide

### Template:

```html
<div class="slide-content">
    <h3>Slide X: Your Title</h3>

    <h4>Section Heading</h4>
    <p>Your explanation text...</p>

    <!-- Inline math -->
    <p>The value function <span class="math">V(s)</span> represents...</p>

    <!-- Display math -->
    <div class="math-box">
        <p><strong>Formula Name:</strong></p>
        <div class="math-display">
            V(s) = \max_a Q(s,a)
        </div>
        <p class="math-note">Explanation of the formula</p>
    </div>

    <!-- Code block (if needed) -->
    <div class="algorithm-box">
        <p><strong>Algorithm:</strong></p>
        <pre><code class="language-python">
def example():
    pass
        </code></pre>
    </div>

    <!-- Learning notes -->
    <div class="learning-note">
        <h4>🤔 My Learning Notes</h4>
        <p>Your personal insights...</p>
    </div>
</div>
```

### Adding the Slide:

1. **Create file**: `slides/slideX.html`
2. **Update index.html**: Add to `slideFiles` array (line 161-166)
   ```javascript
   const slideFiles = [
       'slides/slide1.html',
       'slides/slide2.html',
       'slides/slide3.html',
       'slides/slide4.html',
       'slides/slideX.html'  // Add here
   ];
   ```
3. **Update counter**: Change `totalSlides` (line 160)
   ```javascript
   const totalSlides = 5; // Changed from 4
   ```

---

## 🎨 Styling Classes

### Math Classes:
- `.math` - Inline math (small, inline with text)
- `.math-display` - Display math (centered, larger)
- `.math-box` - Container for formulas with explanations
- `.math-note` - Explanatory text below formulas

### Content Classes:
- `.slide-content` - Wraps entire slide content
- `.algorithm-box` - For algorithms/pseudocode
- `.learning-note` - Personal notes and insights
- `.key-insight` - Highlight important points

---

## 📐 LaTeX Math Reference

### Common Symbols:

| Symbol | LaTeX | Example |
|--------|-------|---------|
| Expected value | `\mathbb{E}[X]` | E[X] |
| Argmax | `\arg\max_a` | argmax_a |
| Sum | `\sum_{i=1}^{n}` | Σ from i=1 to n |
| Square root | `\sqrt{x}` | √x |
| Fraction | `\frac{a}{b}` | a/b |
| Subscript | `Q_t(a)` | Q_t(a) |
| Superscript | `x^2` | x² |
| Greek | `\alpha, \beta, \epsilon` | α, β, ε |
| Indicator | `\mathbb{1}_{A=a}` | 1_{A=a} |

### Advanced:

```latex
<!-- Cases (piecewise functions) -->
A_t = \begin{cases}
    \arg\max_a Q_t(a) & \text{with prob } 1-\varepsilon \\
    \text{random} & \text{with prob } \varepsilon
\end{cases}

<!-- Matrices -->
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}

<!-- Integrals -->
\int_{0}^{\infty} f(x) \, dx

<!-- Limits -->
\lim_{n \to \infty} f(n)
```

Full reference: [KaTeX Supported Functions](https://katex.org/docs/supported.html)

---

## 🔧 How It Works

### Loading Process:

1. **Page loads** → `DOMContentLoaded` event fires
2. **loadSlides()** function runs:
   - Fetches each slide HTML file
   - Creates `<div class="slide">` elements
   - Appends to `#slide-container`
3. **renderMath()** processes all `.math` and `.math-display` elements
4. **Prism.highlightAll()** syntax highlights code blocks

### Navigation:

- **Buttons**: Click "Previous" / "Next"
- **Keyboard**: `←` / `→` arrow keys
- **Auto-scroll**: Smooth scroll to top of slides on change
- **Indicator**: Shows "X / Total" slides

---

## 🚀 Benefits of This Approach

### For Learning:
- 📖 **Clear organization**: Each concept has its own file
- ✏️ **Easy updates**: Modify slides as you learn more
- 🔍 **Beautiful math**: Professional LaTeX rendering
- 💾 **Versioned learning**: Git tracks your learning journey

### For Development:
- 🔧 **Modular**: Easy to maintain and extend
- 🎯 **Focused editing**: Work on one slide at a time
- 🔄 **Reusable**: Copy slide templates to new algorithms
- 🐛 **Easy debugging**: Isolate issues to specific slides

### For Sharing:
- 📱 **Responsive**: Works on all devices
- 🌐 **Static**: No server-side processing needed
- ⚡ **Fast**: Slides load quickly
- 🎨 **Professional**: Beautiful presentation

---

## 💡 Tips

### Math Editing:
1. **Test formulas** at [katex.org](https://katex.org/)
2. **Use `\text{}`** for text inside math: `\text{with probability}`
3. **Escape special chars**: `\{`, `\}`, `\_`
4. **Check browser console** for KaTeX errors

### Slide Content:
- Keep each slide **focused on one concept**
- Use **learning notes** to document your thought process
- Include **examples** and **intuition**
- Link concepts to **math/physics** when possible

### Git Workflow:
```bash
# After editing a slide
git add algorithms/multi-armed-bandit/slides/slide2.html
git commit -m "Update epsilon-greedy explanation in slide 2"

# Easy to see what changed
git diff HEAD~1
```

---

## 🎯 Next Steps

To add more algorithms with this structure:

1. **Copy the template**:
   ```bash
   cp -r algorithms/multi-armed-bandit algorithms/q-learning
   ```

2. **Update slides**:
   - Modify each `slideX.html` with new content
   - Update math formulas for new algorithm

3. **Customize**:
   - Change titles in `index.html`
   - Update Python code
   - Adjust number of slides

4. **Link from main page**:
   - Add algorithm card to root `index.html`

---

## 📞 Questions?

Check the main documentation:
- [README.md](../../README.md)
- [GETTING_STARTED.md](../../GETTING_STARTED.md)
- [PROJECT_SUMMARY.md](../../PROJECT_SUMMARY.md)

---

**Happy Learning! 🚀**

*This modular slide system makes your learning journey organized, beautiful, and shareable!*
