import requests

def get_best_products(api_key, count=5):
    url = f"https://gw.api.alibaba.com/openapi/param2/2/portals.open/api.listPromotionProduct/{api_key}?keywords=&start=0&count=50"
    res = requests.get(url).json().get("result", [])
    sorted_products = sorted(res, key=lambda x: float(x.get("averageScore",0)) * int(x.get("orderCount",0)), reverse=True)
    output = []

    for p in sorted_products[:count]:
        output.append({
            "title": p.get("productTitle"),
            "price": p.get("salePrice"),
            "rating": p.get("averageScore"),
            "link": p.get("productUrl"),
            "image": p.get("imageUrl")
        })
    return output
