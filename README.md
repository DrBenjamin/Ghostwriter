# Ghostwriter

Ghostwriter helps you write academic text.

## Kivy

Setup Kivy Python framework.

```bash
python -m pip install --upgrade pip setuptools virtualenv
```

### Virtual Environment

Setup Virtual Environment.

```bash
python -m virtualenv kivy_venv

# Windows
source kivy_venv/Scripts/activate

# or Linux / Mac
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

Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Build the Apps

Prepare the build.

```bash
buildozer init
```

Edit buildozer.spec file and add requirements.

Install gettext (if missing) on Mac.

```bash
brew install gettext
brew link gettext --force
```

#### Build Mac App

Deploy Mac App.

```bash
# Using PyInstaller and Homebrew (Mac)
brew reinstall --build-from-source sdl2 sdl2_image sdl2_ttf sdl2_mixer
python -m pip install -U pyinstaller
pyinstaller -y --clean --windowed --name Ghostwriter \
  --exclude-module _tkinter \
  --exclude-module Tkinter \
  --exclude-module enchant \
  --exclude-module twisted \
  ./main.py

# or use buildozer
buildozer osx debug deploy
```

#### Build Windows App

Deploy Windows App.

```bash
python -m pip install -U pyinstaller
python -m PyInstaller --hidden-import=collect_submodules --hidden-import=platformdirs.windows --hidden-import=packaging --hidden-import=packaging --hidden-import=packaging.version --hidden-import=packaging.specifiers --hidden-import=packaging.requirements -y --clean --name Ghostwriter --noconsole --onefile ./main.py
```

#### Build Android App

Deploy Android App.

```bash
buildozer android debug deploy
```

#### Build iOS App

Deploy iOS App.

```bash
# Compile the distribution
python -m pip install kivy-ios
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer/
toolchain build python3 kivy

# Create an XCode project
toolchain create ghostwriter ghostwriter

# Compile the app in XCode
open ghostwriter-ios/ghostwriter.xcodeproj
```
