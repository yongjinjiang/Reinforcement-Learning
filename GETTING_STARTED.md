# 🚀 Getting Started Guide

欢迎来到 Reinforcement Learning Journey！这份指南将帮助你快速上手。

## 📋 目录
1. [快速开始](#快速开始)
2. [本地开发](#本地开发)
3. [部署到 GitHub Pages](#部署到-github-pages)
4. [添加新算法](#添加新算法)
5. [常见问题](#常见问题)

---

## 🎯 快速开始

### 方式 1: 直接打开（最简单）

```bash
# 1. 直接用浏览器打开
index.html
```

双击 `index.html` 文件即可！不需要任何服务器。

### 方式 2: 使用本地服务器（推荐）

PyScript 在本地服务器环境下运行更稳定。

```bash
# 使用 Python
python serve.py

# 或者指定端口
python serve.py 3000
```

服务器会自动在浏览器中打开 `http://localhost:8000`

### 方式 3: 使用 VS Code Live Server

1. 安装 "Live Server" 扩展
2. 右键点击 `index.html`
3. 选择 "Open with Live Server"

---

## 💻 本地开发

### 项目结构

```
Reinforcement-Learning/
├── index.html              # 主页（算法列表）
├── css/
│   └── styles.css         # 全局样式
├── js/
│   └── main.js           # 主要 JavaScript
├── algorithms/
│   └── multi-armed-bandit/
│       ├── index.html    # 算法页面（slides + 代码）
│       ├── algorithm.css # 页面样式
│       └── mab_demo.py  # Python 实现
└── assets/
    └── images/          # 图片资源
```

### 开发工作流

1. **编辑内容**
   - HTML: 添加新的 slides 或修改内容
   - CSS: 调整样式和布局
   - Python: 更新算法实现

2. **实时预览**
   - 使用 Live Server 或 `serve.py`
   - 每次保存自动刷新

3. **测试 PyScript**
   - 确保 Python 代码在浏览器中正常运行
   - 检查控制台是否有错误

---

## 🌐 部署到 GitHub Pages

### 步骤 1: 初始化 Git 仓库

```bash
# 初始化仓库
git init

# 添加所有文件
git add .

# 创建首次提交
git commit -m "Initial commit: RL Journey web app"
```

### 步骤 2: 连接到 GitHub

```bash
# 在 GitHub 上创建新仓库（不要初始化 README）
# 然后运行：

git remote add origin https://github.com/你的用户名/Reinforcement-Learning.git
git branch -M main
git push -u origin main
```

### 步骤 3: 启用 GitHub Pages

1. 前往你的 GitHub 仓库
2. 点击 **Settings** (设置)
3. 在左侧菜单中点击 **Pages**
4. 在 "Source" 下:
   - Branch: 选择 `main`
   - Folder: 选择 `/ (root)`
5. 点击 **Save**

### 步骤 4: 访问你的网站

几分钟后，你的网站将在以下地址可用：

```
https://你的用户名.github.io/Reinforcement-Learning/
```

### 后续更新

```bash
# 每次修改后
git add .
git commit -m "描述你的修改"
git push

# GitHub Pages 会自动重新部署（1-2分钟）
```

---

## ➕ 添加新算法

### 快速模板

1. **创建算法文件夹**

```bash
mkdir -p algorithms/q-learning
cd algorithms/q-learning
```

2. **复制模板**

```bash
# 从 multi-armed-bandit 复制模板
cp ../multi-armed-bandit/index.html ./
cp ../multi-armed-bandit/algorithm.css ./
```

3. **修改内容**

在 `index.html` 中：
- 更新标题和描述
- 修改 slides 内容
- 更新 Python 代码

4. **在主页添加卡片**

编辑根目录的 `index.html`，在 algorithm-grid 中添加：

```html
<div class="algorithm-card">
    <div class="card-header">
        <h3>Q-Learning</h3>
        <span class="badge">Completed</span>
    </div>
    <p class="card-description">
        你的算法描述...
    </p>
    <div class="card-topics">
        <span class="topic">主题1</span>
        <span class="topic">主题2</span>
    </div>
    <a href="algorithms/q-learning/index.html" class="card-link">
        Explore Algorithm →
    </a>
</div>
```

5. **测试**

```bash
python serve.py
# 访问新算法页面确保正常工作
```

---

## ❓ 常见问题

### PyScript 代码不运行？

**问题**: 点击 "Run Experiment" 没反应

**解决方案**:
- 确保使用 HTTP 服务器（不是 file:// 协议）
- 检查浏览器控制台是否有错误
- 确保有稳定的网络连接（PyScript 需要下载 Pyodide）

### 样式显示不正确？

**问题**: CSS 样式没有加载

**解决方案**:
- 检查 CSS 文件路径是否正确
- 确保相对路径使用正确（`../../css/styles.css`）
- 清除浏览器缓存后刷新

### GitHub Pages 显示 404？

**问题**: 部署后网站显示 404

**解决方案**:
- 确保 `index.html` 在根目录
- 检查 Settings → Pages 设置是否正确
- 等待 2-5 分钟让部署完成
- 检查 Actions 标签页查看部署状态

### 数学公式显示？

**问题**: 想要显示更复杂的数学公式

**解决方案**: 添加 MathJax 或 KaTeX

在 `<head>` 中添加：

```html
<!-- KaTeX (推荐，更快) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>

<!-- 或者 MathJax -->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
```

---

## 🎨 自定义主题

### 修改颜色方案

编辑 `css/styles.css` 中的 CSS 变量：

```css
:root {
    --primary-color: #2563eb;    /* 主色调 */
    --secondary-color: #7c3aed;  /* 次要色 */
    --accent-color: #f59e0b;     /* 强调色 */
    --bg-color: #0f172a;         /* 背景色 */
    /* ... 更多颜色 */
}
```

### 添加亮色主题

```css
/* 添加到 styles.css */
@media (prefers-color-scheme: light) {
    :root {
        --bg-color: #ffffff;
        --text-color: #1e293b;
        /* ... 其他亮色变量 */
    }
}
```

---

## 📚 学习资源

### 推荐阅读
- [Sutton & Barto - Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book.html)
- [OpenAI Spinning Up](https://spinningup.openai.com/)
- [DeepMind x UCL RL Course](https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021)

### 相关工具
- [PyScript Docs](https://docs.pyscript.net/)
- [Prism.js](https://prismjs.com/)
- [GitHub Pages Guide](https://pages.github.com/)

---

## 🤝 贡献

欢迎贡献！如果你想：
- 修复 bug
- 添加新算法
- 改进文档
- 提出建议

请：
1. Fork 这个项目
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

---

## 💡 提示和技巧

### 1. 使用浏览器开发者工具
- `F12` 打开开发者工具
- 查看控制台了解 PyScript 加载状态
- 使用 Network 标签检查资源加载

### 2. Keyboard Shortcuts（算法页面）
- `←` / `→`: 上一张/下一张 slide
- `Ctrl+Shift+I`: 打开开发者工具

### 3. 性能优化
- 图片使用 WebP 格式并压缩
- 考虑使用 CDN 加速库文件
- 延迟加载非首屏内容

### 4. SEO 优化
- 为每个页面添加 `<meta>` 描述
- 使用语义化 HTML 标签
- 添加 `sitemap.xml`

---

## 📞 获取帮助

如果遇到问题：

1. **检查文档**: 先看 README.md 和本文档
2. **搜索 Issues**: 查看 GitHub Issues 是否有类似问题
3. **创建 Issue**: 在 GitHub 上创建新 issue
4. **社区讨论**: 加入相关 Discord/Slack 社区

---

**祝你学习愉快！🚀**

*最后更新: 2024年11月*
