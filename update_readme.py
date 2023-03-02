import feedparser 
poeun_blog_rss_url = "https://ingu627.github.io/feed.xml" 
rss_feed = feedparser.parse(poeun_blog_rss_url)

latest_blog_post_list = "" 

MAX_POST_NUM = 5

for idx, feed in enumerate(rss_feed['entries']): 
    if idx > MAX_POST_NUM: 
        break 
    feed_date = feed['published_parsed'] 
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n" 

markdown_text = """
<!--
**ingu627/ingu627** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
<p align="center">
 <h2 align="center">🙋‍♂️ Hi, I'm Hyunseok.</h2>
 <h3 align="center">I am very motivated to experience the world in so many different ways.</h3>
</p>

<div align=center>
 <img src=https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fingu627&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false>
</div>

<h2 align="center">💎 Github Commit</h2>

<p align = "center">
  <img src="https://github-readme-stats.vercel.app/api?username=ingu627&show_icons=true&theme=radical">
</p>
<!--   ![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=anuraghazra&show_icons=true&theme=radical) -->

<p align="center">
<h2 align="center">🏅 CERTIFICATES</h2>
<h4 align="center"> Big-Data Analysis Engineer (2021.12) | Engineer Quality Management (2021.06) | Survey Analyst, Junior (2020.11) | Advanced Data Analytics Semi-Professional (2021.06) | Structured Query Language Developer (2021.10) | Artificial Intelligence of Things (2021.01) | DSAC Expert (2021.01) | Computer Specialist in Spreadsheet & Database Level-Ⅰ (2021.03) | Word Processor Specialist (2021.07) | 6-SIGMA Green Belt (2021.02) | Azure AI Fundamentals (2021.12) | Azure Fundamentals (2022.01) | Azure Data Fundamentals (2022.03) | Google Analytics Individual Qualification (2021.09)</h3>
</p>

<h2 align="center">💬 MORE INFO! </h2>

<div align=center>
 <a href="https://ingu627.github.io/">
  <img src=https://img.shields.io/badge/-Tech%20blog-black?style=flat-square&logo=github&link=https://ingu627.github.io/>
 </a>
 <a href="https://www.linkedin.com/in/ingu627/">
  <img src=https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/ingu627/>
 </a>
 <a href="mailto:rjsdudans@naver.com">
  <img src=https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=mailto:rjsdudans@naver.com>
 </a>
</div>

<br/>
<br/>
<br/>
<h2>📚 Latest Blog Post</h2>


""" 

readme_text = f"{markdown_text}{latest_blog_post_list}" 

with open("README.md", 'w', encoding='utf-8') as f: 
    f.write(readme_text)
