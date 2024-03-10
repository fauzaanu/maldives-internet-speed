# Internet Speeds in Maldives

Comparing all the internet speeds in maldives along with max possible GB, Rate of price per GB and so on

[Max GB Comparison](https://github.com/fauzaanu/maldives-internet-speed/blob/main/max_gb.csv)

[Max Value (Price / GB) Comparison](https://github.com/fauzaanu/maldives-internet-speed/blob/main/max_value.csv)

[results](https://github.com/fauzaanu/maldives-internet-speed/blob/main/result.csv)

[results simplified](https://github.com/fauzaanu/maldives-internet-speed/blob/main/result_simple.csv)

## How to choose an internet package 101

1. You download a lot of stuff constantly
   - Go for the highest GB possible plans, comparison and choose something.
2. You dont download a lot normally, and download once in a while
   - Much better to go for the lowest package to get 5M after throttle
   - And use a booster or a datapack for the downloads
3. You need best value per GB
   - Supernet 10M and FIBRE 10M gets you 1.5TB GB for the lowest price
   - Going below that sets your speed at 2M and sets max possible GB at 600-ish GB and threfore, may not be that ideal

### Starlink

While calculating for starlink it was assumed that 1TB is available at 200M and the rest are available at 1M
Source: (send a correction if this is wrong)
1. https://arstechnica.com/tech-policy/2022/11/starlink-to-cap-users-at-1tb-of-high-speed-data-unless-they-pay-extra/

Another point to note in starlink is that the 200M will not be consistent through out the month
Also an important point is the setup cost is around 7x more than a normal setup cost of a local provider

## Usage

This script is written in vanilla python only. (This script was written without any internet connection right after
changing homes. I just wanted to see a comparison)

To run this update the `data.csv` with the initial data from your sources and run `main.py` with python to
get `result.csv`
and `result_simple.csv`

If there are mistakes or if you add some new plans, please do send a pull request :)