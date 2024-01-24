from django.shortcuts import render

posts = {
        "post1": {
            "for_sale": False,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Fancy Product",
            "special_or_popular": False,
            "old_price": "",
            "new_price": "$40.00 - $80.00",
            "product_action": "View options"
        },
        "post2": {
            "for_sale": True,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Special Item",
            "special_or_popular": True,
            "old_price": "$20.00",
            "new_price": "$18.00",
            "product_action": "Add to card"
        },
        "post3": {
            "for_sale": True,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Sale Item",
            "special_or_popular": False,
            "old_price": "$50.00",
            "new_price": "$25.00",
            "product_action": "Add to card"
        },
        "post4": {
            "for_sale": False,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Popular Item",
            "special_or_popular": True,
            "old_price": "",
            "new_price": "$40.00",
            "product_action": "Add to card"
        },
        "post5": {
            "for_sale": True,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Sale Item",
            "special_or_popular": False,
            "old_price": "$50.00",
            "new_price": "$25.00",
            "product_action": "Add to card"
        },
        "post6": {
            "for_sale": False,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Fancy Product",
            "special_or_popular": False,
            "old_price": "",
            "new_price": "$120.00 - $280.00",
            "product_action": "View options"
        },
        "post7": {
            "for_sale": True,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Special Item",
            "special_or_popular": True,
            "old_price": "$20.00",
            "new_price": "$18.00",
            "product_action": "Add to card"
        },
        "post8": {
            "for_sale": False,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Popular Item",
            "special_or_popular": True,
            "old_price": "",
            "new_price": "$40.00",
            "product_action": "Add to card"
        },
    }

def home(request):
    return render(request, 'home.html', context={"posts": posts, "title_name": "Shop in style"})
