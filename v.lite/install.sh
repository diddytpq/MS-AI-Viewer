#!/bin/bash
CURRENT_DIR="$(pwd)"

mkdir "${CURRENT_DIR}/install"

cd "${CURRENT_DIR}/install"

echo "#!/bin/bash
cd \"${CURRENT_DIR}\"
python3 \"${CURRENT_DIR}/login.py\"" > main.sh

chmod +x main.sh

# 생성한 sh 파일을 실행하는 .desktop 파일을 생성합니다.
echo "[Desktop Entry]
Encoding=UTF-8
Name=MS-AI-Viewer-Lite
Type=Application
Path=${CURRENT_DIR}
Icon=${CURRENT_DIR}/ui/images/icon2.png
Exec=${CURRENT_DIR}/install/main.sh
Terminal=True" > ms-ai-Lite.desktop

# 생성한 .desktop 파일을 /usr/share/applications 경로로 복사합니다.
sudo cp ms-ai-Lite.desktop /usr/share/applications/
