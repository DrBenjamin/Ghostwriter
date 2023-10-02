# Ghostwriter

Ghostwriter helps you write academic text.

## Kivy Configuration

Setup Kivy Python framework.

```bash
python -m pip install --upgrade pip setuptools virtualenv
```

### Virtual Environment

Setup Virtual Environment.

```bash
python -m virtualenv kivy_venv
source kivy_venv/Scripts/activate
# or on Linux & Mac
source kivy_venv/bin/activate
```

### Install Kivy

Install Kivy. Download pre-compiled wheel from https://github.com/kivy/kivy/releases

```bash
python -m pip install <filename>
```

or install from sources

```bash
python -m pip install "kivy[base]" kivy_examples
```

### Install buildozer (Android)

Install buildozer.

```bash
python -m pip install buildozer
```

### Build Android App

Prepare Android build.

```bash
buildozer init
```

Edit buildozer.spec file to add requirements.

Install gettext (if missing).

```bash
brew install gettext
brew link gettext --force
```

Deploy Android App.

```bash
buildozer android debug deploy
```
