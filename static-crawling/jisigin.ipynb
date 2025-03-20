{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 네이버 지식인 페이지 정적 크롤링\n",
    "정적 크롤링을 통해 네이버 지식인 페이지에서 데이터를 추출하는 방법을 학습합니다."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. 필요한 라이브러리 설치 및 임포트\n",
    "먼저, 웹 크롤링을 위해 필요한 라이브러리들을 설치하고 임포트합니다.\n",
    "\n",
    "- bs4: BeautifulSoup 라이브러리는 HTML/XML 페이지를 파싱하여 데이터를 쉽게 추출할 수 있게 도와줍니다.\n",
    "- requests: HTTP 요청을 보내 웹 페이지의 HTML을 받아오는 라이브러리입니다.\n",
    "- pandas: 데이터를 표 형태로 처리하고, 엑셀 파일로 저장하는 데 사용됩니다.\n",
    "- openpyxl: pandas가 엑셀 파일을 처리할 수 있도록 도와주는 라이브러리입니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install bs4\n",
    "!pip install requests\n",
    "!pip install pandas\n",
    "!pip install openpyxl"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2. HTML 페이지 불러오기 및 파싱\n",
    "이제 웹 페이지를 불러와서 HTML을 파싱하여 필요한 데이터를 추출하는 작업을 시작합니다.\n",
    "\n",
    "- requests.get(url): 지정한 URL에 HTTP GET 요청을 보냅니다.\n",
    "- BeautifulSoup(html, 'html.parser'): 응답 받은 HTML을 BeautifulSoup을 사용해 파싱합니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "\n",
    "# 네이버 지식인 삼성전자 검색 페이지 URL\n",
    "url = \"https://kin.naver.com/search/list.naver?query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90\"\n",
    "response =   # 요청 보내기\n",
    "html =   # 응답 받은 HTML 문서\n",
    "soup =   # BeautifulSoup으로 파싱\n",
    "soup"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3. 특정 HTML 요소 선택\n",
    "크롤링할 HTML 요소를 선택하기 위해 CSS 선택자를 사용하여 데이터를 추출합니다.\n",
    "\n",
    "- soup.select_one(): CSS 선택자를 사용하여 첫 번째 일치하는 요소를 선택합니다.\n",
    "- tree: 선택된 HTML 요소(첫 번째 질문)에 대한 정보를 담고 있습니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 첫 번째 질문 요소 선택\n",
    "tree = \n",
    "tree  # 첫 번째 질문의 HTML 구조를 출력하여 확인"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4. 정보 추출: 제목, 링크, 날짜, 카테고리, 답변수\n",
    "선택한 HTML 요소에서 원하는 데이터를 추출합니다.\n",
    "\n",
    "- title_tag.text: title_tag 요소에서 텍스트(제목)를 추출합니다.\n",
    "- title_tag.attrs['href']: title_tag 요소에서 링크를 추출합니다.\n",
    "- date_tag.text, category_tag.text: 각각 작성일과 카테고리를 추출합니다.\n",
    "- hit_tag.text.split(): 답변수를 추출하고 불필요한 문자를 제거합니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 제목과 링크 추출\n",
    "title_tag = \n",
    "title = \n",
    "link = \n",
    "print(title, link)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 날짜 추출\n",
    "date_tag = \n",
    "date = \n",
    "print(date)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 카테고리 추출\n",
    "category_tag = \n",
    "category = \n",
    "print(category)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "# 조회수 추출\n",
    "hit_tag = \n",
    "texts = \n",
    "# hit = \n",
    "print(hit)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5. 한 페이지에서 모든 질문 정보 추출\n",
    "한 페이지에 여러 질문이 있을 때, 모든 질문의 정보를 추출합니다.\n",
    "\n",
    "- soup.select(): 여러 개의 요소를 선택하여 리스트로 반환합니다.\n",
    "- 각 질문에 대해 for 루프를 돌며 제목, 링크, 날짜, 카테고리, 조회수를 추출합니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 여러 질문 정보 추출\n",
    "trees = soup.select(\".basic1 > li > dl\")\n",
    "for tree in trees:\n",
    "    title = tree.select_one(\"._nclicks\\\\:kin\\\\.txt\").text\n",
    "    link = tree.select_one(\"._nclicks\\\\:kin\\\\.txt\").attrs['href']\n",
    "    date = tree.select_one(\".txt_inline\").text\n",
    "    category = tree.select_one(\"._nclicks\\\\:kin\\\\.cat2\").text\n",
    "    hit = tree.select_one(\".hit\").text.split()[1]\n",
    "    \n",
    "    # 출력\n",
    "    print(title, link, date, category, hit)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 6. 여러 페이지 크롤링\n",
    "페이지를 변경하면서 여러 페이지의 데이터를 크롤링합니다.\n",
    "\n",
    "- for page_num in range(1, 4): 1페이지부터 3페이지까지 순차적으로 크롤링합니다.\n",
    "- 각 페이지에서 데이터를 추출하여 data 리스트에 추가하고, 이를 pandas DataFrame으로 변환하여 엑셀 파일로 저장합니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 여러 페이지에서 정보 추출\n",
    "data = []\n",
    "for page_num in range(1, 4):  # 1~3페이지 크롤링\n",
    "    url = f\"https://kin.naver.com/search/list.naver?query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&page={page_num}\"\n",
    "    response = requests.get(url)\n",
    "    html = response.text\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "    trees = soup.select(\".basic1 > li > dl\")\n",
    "    \n",
    "    for tree in trees:\n",
    "        ################\n",
    "        \n",
    "        # 데이터를 리스트에 추가\n",
    "        data.append([title, link, date, category, hit])\n",
    "\n",
    "# DataFrame으로 변환\n",
    "import pandas as pd\n",
    "df = "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 7. 결과 저장\n",
    "위의 크롤링한 데이터를 엑셀 파일로 저장합니다.\n",
    "\n",
    "- df.to_excel(): 추출한 데이터를 엑셀 파일로 저장합니다. index=False를 설정하여 인덱스를 제외하고 저장합니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# pandas를 사용해 엑셀로 저장"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
