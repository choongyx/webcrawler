# E-commerce Web Crawler

1. Install all the required packages:
   - `pip install requests` 
   - `pip install 'beautifulsoup4==4.8.1'` 
   - `pip install json` 
   - `pip install parsel`
2. Run the program with the command `python main.py`.
3. Input the product that you want to compare prices for and the maximum number of results that you want from each website when prompted, as demonstrated in the image below. 
4. Example Output: ![Program Output](/output.png)

**Note:** Since Lazada adopted a security feature that prevents bot from accessing and being on the site, if you run the program too often, there won't be any results from lazada. To avoid this, try to run the program after a time interval between each run, say 1 minute.
