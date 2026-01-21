# MLOps Milestone 0: Reproducible Environment and CI Configuration
This project is a milestone task for Module 1 of the MLOps course. The core objective is to establish a **reproducible Python environment** and an **automated CI workflow**, addressing the "it works on my machine" problem in production ML systems.

### Local Environment Setup
1. clone github：`git clone https://github.com/jane872/UIC-ids568-milestone0`
2. cd：`cd UIC-ids568-milestone0`
3. Create a virtual environment：`python3 -m venv venv`
4. Activate environment：
   - Windows：`venv\Scripts\activate`
   - macOS/Linux：`source venv/bin/activate`
5. Install dependencies：`pip install -r requirements.txt`
6. test：`pytest3 -v`


 
### badge test
[![MLOps Milestone 0 CI](https://github.com/jane872/UIC-ids568-milestone0/actions/workflows/ci.yml/badge.svg)](https://github.com/jane872/UIC-ids568-milestone0/actions/workflows/ci.yml)

