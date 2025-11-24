# English Spelling App - Android

A spelling practice application for Android, built with Kivy and Python.

## Features

- ▶ **Hear New Word**: Listen to a randomly selected word
- 🔁 **Replay**: Replay the current word
- 👁 **Show Word**: Reveal the spelling
- 📂 **Load Words**: Upload your own `words.txt` file from your device

## Building the APK

### Option 1: GitHub Actions (Recommended)

1. **Push this code to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **The workflow will automatically build the APK** when you push to `main` or `master` branch

3. **Download the APK**:
   - Go to your repository on GitHub
   - Click the **Actions** tab
   - Click on the latest workflow run
   - Scroll down to **Artifacts**
   - Download `spelling-app-debug.apk`

4. **Manual trigger** (optional):
   - Go to **Actions** tab
   - Select "Build Android APK" workflow
   - Click **Run workflow** → **Run workflow**

### Option 2: Build Locally (Advanced)

**Requirements**: Linux or WSL with Python 3.11+

```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install -y git zip unzip openjdk-17-jdk autoconf libtool \
  pkg-config zlib1g-dev libncurses-dev cmake libffi-dev libssl-dev \
  liblzma-dev uuid-dev

# Install Buildozer
pip install buildozer cython

# Build APK
buildozer android debug
```

The APK will be in `bin/` directory.

## Installing on Your Phone

1. Download the `.apk` file to your Android device
2. Enable "Install from Unknown Sources" in Settings
3. Open the APK file and install
4. Grant storage permissions when prompted (needed for file picker)

## Adding Words

1. Create a `words.txt` file with one word per line
2. Open the app
3. Tap **📂 Load Words File**
4. Select your `words.txt` file
5. Start practicing!

## License

MIT License - See `main.py` for details
