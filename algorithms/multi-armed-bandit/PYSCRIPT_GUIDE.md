# 🐍 PyScript Integration Guide

## Overview

This algorithm page uses **PyScript** to run Python code directly in your browser, enabling interactive demonstrations of the Multi-Armed Bandit algorithms.

---

## ✅ What's Been Fixed

### Issue: NumPy Module Not Found
**Error Message**:
```
ModuleNotFoundError: The module 'numpy' is included in the Pyodide distribution,
but it is not installed.
```

**Solution Applied**:
1. ✅ Added PyScript configuration in [index.html:25-27](index.html)
2. ✅ Embedded Python code directly in [slide4.html](slides/slide4.html)
3. ✅ Auto-loads NumPy when page loads

---

## 🔧 How It Works

### Configuration (index.html)

```html
<!-- PyScript Configuration -->
<script type="py-config">
    packages = ["numpy"]
</script>
```

This tells PyScript to automatically load NumPy when the page loads.

### Python Code Execution (slide4.html)

```html
<!-- PyScript code block -->
<script type="py" terminal>
import numpy as np
from js import document

# Your Python code here...
def run_experiment():
    # ...

# Auto-run on page load
run_experiment()
</script>
```

The `terminal` attribute enables console output for debugging.

---

## 🚀 Running the Code

### Method 1: Automatic (Default)
When you navigate to slide 4, the code runs automatically:
1. Page loads
2. PyScript downloads NumPy (first time only, ~1-2 seconds)
3. Python code executes
4. Results display in output box

### Method 2: Manual Re-run
Click the **"▶ Run Experiment"** button to run again with a new random seed.

---

## 🐛 Troubleshooting

### 1. "Loading Python..." Message Stuck

**Cause**: Slow network or PyScript still downloading

**Solution**:
- Wait 5-10 seconds on first load
- Check browser console (F12) for errors
- Ensure stable internet connection (PyScript downloads from CDN)

### 2. Code Not Running

**Symptoms**: Button clicks do nothing

**Solutions**:
- ✅ Use local server: `python serve.py` (NOT `file://` protocol)
- ✅ Check browser console for JavaScript errors
- ✅ Try hard refresh: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)

### 3. NumPy Import Error

**Error**: `ModuleNotFoundError: No module named 'numpy'`

**Check**:
```html
<!-- Should be in index.html <head> -->
<script type="py-config">
    packages = ["numpy"]
</script>
```

If missing, add it after the PyScript script tag.

### 4. Browser Compatibility

**Supported Browsers**:
- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)

**Not Supported**:
- ❌ Internet Explorer
- ❌ Very old browser versions

---

## 📊 Performance Notes

### First Load
- Downloads PyScript runtime (~5 MB)
- Downloads NumPy package (~10 MB)
- **Total**: ~15 MB, one-time download
- **Time**: 2-10 seconds depending on connection

### Subsequent Loads
- Uses browser cache
- **Time**: < 1 second

### Code Execution
- Runs 1000 simulation steps
- **Time**: ~100-200ms (very fast!)

---

## 🎨 Customizing the Code

You can modify the experiment parameters directly in [slide4.html](slides/slide4.html):

### Change Number of Steps
```python
# Line ~215
def run_experiment(steps=1000):  # Change 1000 to any number
```

### Add New Agent
```python
# Line ~220
agents = {
    'ε-greedy (ε=0.1)': EpsilonGreedyAgent(10, epsilon=0.1),
    'ε-greedy (ε=0.01)': EpsilonGreedyAgent(10, epsilon=0.01),
    'UCB (c=2)': UCBAgent(10, c=2),
    'YOUR NEW AGENT': YourAgent(10, param=value)  # Add here
}
```

### Change Number of Arms
```python
# Line ~217
bandit = Bandit(k_arms=10)  # Change 10 to any number
```

---

## 🔍 Debugging Tips

### Enable Console Output

The code already has `print()` statements:
```python
print("📦 Loading Multi-Armed Bandit simulation...")
print("✅ Experiment completed!")
```

**To see them**:
1. Open browser console: `F12` → Console tab
2. Look for output with PyScript prefix

### Add Your Own Debugging

```python
# In slide4.html, add anywhere in the code
print(f"Debug: bandit values = {bandit.true_values}")
print(f"Debug: agent Q = {agent.Q}")
```

### Check PyScript Status

```javascript
// In browser console
console.log(pyscript);  // Shows PyScript object
```

---

## 📚 PyScript Resources

### Official Documentation
- [PyScript Docs](https://docs.pyscript.net/)
- [Pyodide Docs](https://pyodide.org/)
- [Supported Packages](https://pyodide.org/en/stable/usage/packages-in-pyodide.html)

### Examples
- [PyScript Examples](https://pyscript.com/@examples)
- [PyScript Cookbook](https://jeff.glass/post/pyscript-cookbook/)

---

## 🎯 Code Structure

### Classes Implemented

1. **Bandit**
   - Environment with K arms
   - Gaussian reward distribution
   - Tracks optimal action

2. **EpsilonGreedyAgent**
   - ε-greedy policy
   - Incremental value updates
   - Configurable step size

3. **UCBAgent**
   - Upper Confidence Bound selection
   - Deterministic exploration
   - Logarithmic regret bound

### Main Function

**`run_experiment(steps=1000)`**
- Creates bandit environment
- Initializes multiple agents
- Runs simulation for specified steps
- Computes performance metrics
- Displays results in output box

---

## 💡 Advanced Usage

### Loading Additional Packages

Edit `index.html`:
```html
<script type="py-config">
    packages = ["numpy", "matplotlib", "pandas"]
</script>
```

**Available packages**: Most scientific Python packages available in Pyodide.

### Creating Visualizations

```python
import matplotlib.pyplot as plt

# Create plot
plt.figure()
plt.plot(rewards)
plt.title("Rewards over Time")

# Display in page
from js import document
img = plt.gcf().canvas.tostring_rgb()
# ... render to HTML element
```

**Note**: Matplotlib visualization requires additional setup.

---

## 🚦 Status Indicators

### What You Should See

#### On Page Load:
```
📦 Loading Multi-Armed Bandit simulation...
🎯 EXPERIMENT RESULTS (1000 steps)
==================================================

📊 ε-greedy (ε=0.1):
   Average Reward: 1.234
   Optimal Action: 85.5%

📊 ε-greedy (ε=0.01):
   Average Reward: 0.987
   Optimal Action: 72.3%

📊 UCB (c=2):
   Average Reward: 1.456
   Optimal Action: 91.2%

==================================================
🎖️  Best Possible Reward: 1.678
🎲 Number of Arms: 10
```

#### In Console:
```
✅ Ready! Click 'Run Experiment' to run again with different random seed.
```

---

## 🔒 Security Note

PyScript runs Python code in a **sandboxed environment** (WebAssembly):
- ✅ Cannot access your file system
- ✅ Cannot run system commands
- ✅ Cannot access other browser tabs
- ✅ Safe to run untrusted code (within reason)

---

## ⚡ Quick Reference

| Task | Command |
|------|---------|
| Start local server | `python serve.py` |
| Open browser console | `F12` → Console |
| Hard refresh | `Ctrl+Shift+R` |
| Edit slide code | Open `slides/slide4.html` |
| Check PyScript config | See `index.html` line 25-27 |

---

## 📞 Getting Help

If you encounter issues:

1. **Check this guide** - Most common issues covered
2. **Browser console** - Look for error messages
3. **PyScript docs** - [docs.pyscript.net](https://docs.pyscript.net/)
4. **GitHub Issues** - Search for similar problems

---

**Happy Experimenting! 🚀**

*The beauty of PyScript: Python in the browser, no backend needed!*
