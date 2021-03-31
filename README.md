# Senator Trading
The STOCK Act (Stop Trading on Congressional Knowledge) was signed into law by President Barack Obama in 2012. This law prevents insider trading by members of Congress and other government employees that may have access to non-public information. As a result, every Senator is required to publicly file any transaction of stock, bond, commodities futures, and other securities within 45 days.

Disclosures can be found here: https://efdsearch.senate.gov/
Tableau Dashboard can be found here: https://public.tableau.com/views/SenatorTrading/TradingDashboard?:language=en&:display_count=y&:origin=viz_share_link

Data was collected using a Python script with the Selenium and Pandas modules. The script accessed the site and scrolled through all electronically submitted disclosures, adding each to a data frame.