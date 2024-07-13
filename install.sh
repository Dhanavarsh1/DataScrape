python3 -m venv venv
source venv/bin/activate
pip install TikTokApi
pip install --force-reinstall -v "playwright==1.30.0"
playwright install
