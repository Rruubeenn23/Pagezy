import os
import sys

# 👉 AÑADIR el path raíz del proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models_publicos import ProductoBase

app = create_app()

with app.app_context():
    productos = [
        ProductoBase(
            tipo="Super",
            nombre="Black Ice DragonFruit Strawberry",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/BLACK-ICE-DRAGONFRUIT-STRAWBERRY-600x600.png"
        ),ProductoBase(
            tipo="Super",
            nombre="Blue Razz",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/BLUE-RAZZ-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Blueberry Blackcurrant Ice",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/02/blueberry-blackcurrant-ice-2-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Blueberry Cherry Cola",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/BLUEBERRYCHERRY-COLA-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Blueberry Cherry Cranberry",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/BLUEBERRY-CHERRY-CRANBERRY-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Blueberry Ice",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/BLUEBERRY-ICE-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Double Apple",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/DOUBLE-APPLE-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Lemon Lime",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/LEMON-LIME-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Mixed Berry",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/MIXED-BERRY-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Peach Mango Pineapple",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/02/peach-mango-pineapple-1-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Pink Lemonade",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/02/pink-lemonade-1-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Raspberry Watermelon",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/RASPBERRY-WATERMELON-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Red Bull",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/RED-BULL-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Skittles",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/SKITTLES-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Strawberry Banana",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/STRAWBERRY-BANANA-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Strawberry Ice",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/02/strawberry-ice-1-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Strawberry Kiwi",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/STRAWBER-KIWI-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Strawberry Vainilla Cola",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/02/strawberry-vanilla-cola-1-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Red Bull",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/SUMMER-DREAM-600x600.png"
        ),
        ProductoBase(
            tipo="Super",
            nombre="Watermelon Ice",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/SUMMER-DREAM-600x600.png"
        ),





        #GALAXY
        ProductoBase(
            tipo="Galaxy",
            nombre="Black Ice DragonFruit Strawberry",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/6BLACKICEDRAGONFRUITSTRAWBERRY%E9%BB%91%E5%86%B0%E7%81%AB%E9%BE%99%E6%9E%9C%E8%8D%89%E8%8E%93.png"
        ),
        ProductoBase(
            tipo="Galaxy",
            nombre="bLUE rAZZ",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/2BLUERAZZ%E8%93%9D%E8%8E%93%E6%8B%89%E5%85%B9.png"
        ),
        ProductoBase(
            tipo="Galaxy",
            nombre="Lemon Lime",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/5LEMONLIME%E6%9F%A0%E6%AA%AC%E9%9D%92%E6%9F%A0.png"
        ),
        ProductoBase(
            tipo="Galaxy",
            nombre="Lemon Peach",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/7LEMONPEACH%E6%9F%A0%E6%AA%AC%E6%A1%83%E5%AD%90.png"
        ),
        ProductoBase(
            tipo="Galaxy",
            nombre="Pineapple Coconut",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/3PINEAPPLECOCONUT%E8%8F%A0%E8%90%9D%E6%A4%B0%E5%AD%90.png"
        ),
        ProductoBase(
            tipo="Galaxy",
            nombre="Raspberry Watermelon",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/1RASPBERRYWATERMELON%E6%A0%91%E8%8E%93%E8%A5%BF%E7%93%9C.png"
        ),
        ProductoBase(
            tipo="Galaxy",
            nombre="Strawberry Banana",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/11STRAWBERRYBANANA%E8%8D%89%E8%8E%93%E9%A6%99%E8%95%89.png"
        ),
        ProductoBase(
            tipo="Galaxy",
            nombre="Strawberry Kiwi",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/9STRAWBERRYKIWI%E8%8D%89%E8%8E%93%E5%A5%87%E5%BC%82%E6%9E%9C.png"
        ),
        ProductoBase(
            tipo="Galaxy",
            nombre="Strawberry Raspberry Cherry Ice",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/8STRAWBERRYRASPBERRYCHERRYICE%E8%8D%89%E8%8E%93%E6%A0%91%E8%8E%93%E6%A8%B1%E6%A1%83%E5%86%B0.png"
        ),
        ProductoBase(
            tipo="Galaxy",
            nombre="Strawberry Red Bull",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/10STRAWBERRYREDBULL%E8%8D%89%E8%8E%93%E7%BA%A2%E7%89%9B.png"
        ),
        ProductoBase(
            tipo="Galaxy",
            nombre="Triple Melon",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/12TRIPLEMELON%E4%B8%89%E9%87%8D%E8%9C%9C%E7%93%9C.png"
        ),
        ProductoBase(
            tipo="Galaxy",
            nombre="Watermelon Ice",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/4WATERMELONICE%E8%A5%BF%E7%93%9C%E5%86%B0.png"
        ),




        #TRIPLE
        ProductoBase(
            tipo="Triple",
            nombre="BlackCurrant Ice + Pink Lemonade + Kiwi Passion Fruit Guava",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/blackcurrant-ice-pink-lemonade-kiwi-passion-fruit-guava-600x600.png"
        ),
        ProductoBase(
            tipo="Triple",
            nombre="Blueberry Sour Raspberry + Strawberry Mango + Lemon Cola",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/Bluberry-soue-rasberry-strawberry-mango-lemon-cola-600x600.png"
        ),
        ProductoBase(
            tipo="Triple",
            nombre="Kiwi Passion Fruit + Love 66 + Vanilla",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/Kiwi-passions-fruit-Love-66-Vanilla-1-600x600.png"
        ),
        ProductoBase(
            tipo="Triple",
            nombre="Lemon Lime `Strawberry Watermelon + Blueberry Ice",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/LEMON-LIME-STRAWBERRY-WATERMELON-BLUEBERRY-ICE-600x600.png"
        ),
        ProductoBase(
            tipo="Triple",
            nombre="Peach Berry + Black Ice + Strawberry Vanilla Cola",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/peach-berry-black-ice-starwberry-vanilla-cola-600x600.png"
        ),
        ProductoBase(
            tipo="Triple",
            nombre="Peach Ice + Dragon Fruit Ice + Mix Fruit",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/Peach-ice-dragon-fruit-ice-mix-fruit-600x600.png"
        ),
        ProductoBase(
            tipo="Triple",
            nombre="Pineapple Coconut + Strawberry Banana + Blue Razz",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/PINEAPPLE-COCONUT-STRAWBERRY-BANANA-BLUE-R-AZZ-600x600.png"
        ),
        ProductoBase(
            tipo="Triple",
            nombre="Raspberry Watermelon + Mango Peach + Strawberry Kiwi",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/RASPBERRY-WATERMELON-MANGO-PEACH-STRAWBERRY-KIWI-600x600.png"
        ),
        ProductoBase(
            tipo="Triple",
            nombre="Strawberry Banana ` Raspberry Watermelon + Lemon Lime",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/STRAWBERRY-BANANA-RASPBERRY-WATERMELON-LEMON-LIME-600x600.png"
        ),
        ProductoBase(
            tipo="Triple",
            nombre="Strawberry Kiwi + Sour Mango Pineapple + Red Bull",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/STRAWBERRY-KIWI-SOUR-MANGO-PINEAPPLE-RED-BULL-600x600.png"
        ),
        ProductoBase(
            tipo="Triple",
            nombre="Strawberry Raspberry + Triple Melon + Sour Mango Pineapple",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/STRAWBERRY-RASPBERRY-TRIPLE-MELON-SOUR-MANGO-PINEAPPLE-600x600.png"
        ),
        ProductoBase(
            tipo="Triple",
            nombre="Strawberry Vanilla Coke + Blueberry Raspberry + Lemon Lime",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/STRAWBERRY-VANILLA-COKE-BLUEBERRY-RASPBERRY-LEMON-LIME-600x600.png"
        ),
        ProductoBase(
            tipo="Triple",
            nombre="Tropical Fruit + Strawberry Watermelon + Lemon Peach",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/TROPICAL-FRUIT-STRAWBERRY-WATERMELON-LEMON-PEACH-600x600.png"
        ),
        ProductoBase(
            tipo="Triple",
            nombre="Watermelon Ice + Red Bull + Strawberry Kiwi",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/WATERMELON-ICE-RED-BULL-STRAWBERRY-KIWI-600x600.png"
        ),
        ProductoBase(
            tipo="Triple",
            nombre="Watermelon Ice + Strawberry Ice Cream + Triple Melon",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/WATERMELON-ICE-STRAWBERRY-ICECREAM-TRIPLE-MELON-600x600.png"
        ),





        #TWINS
        ProductoBase(
            tipo="Twins",
            nombre="Black Ice Dragon Fruit Strawberry + Raspberry Watermelon",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/09/Black-ice-dragon-fruit-strawberry-Raspberry-watermelon.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Blue Razz Lemonade + Lemon Lime",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/blue-razz-lemonadelemon-lime-2-600x600.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Blueberry Blackcurrant + GrapeFruit Refresher",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/Blueberry-Blackurrant-Grapefruit-Refresher-600x600.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Blueberry Ice + Fizzy Cherry",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/blueberry-ice-fizzy-cherry-1-600x600.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Cherry Cola + Juicy Peach Ice",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/Cherry-Cola-Juicy-Peach-Ice-600x600.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Grape Ice + Strawberry Kiwi",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/grape-ice-strawberry-kiwi-1-600x600.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Lemon Lime + Watermelon Ice",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/lemon-lime-watermelon-1-600x600.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Orange mango Watermelon + Red Bull",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/orange-mango-watermelon-redbull-1-600x600.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Passion Fruit Mojito + Triple Mint",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/Passion-Fruit-Mojito-Triple-Mint-600x600.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Pineapple Coconut + Strawberry Banana",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/pineapple-coconut-strawberry-banana-1-600x600.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Pineapple Coconut + Watermelon Ice",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/09/Pineapple-coconut-watermelon-ice.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Strawberry Banana + Fizzy Cherry",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/STRAWBERRY-BANANAFIZZY-CHERRY1-1-600x600.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Strawberry Ice + Mango Peach Watermelon",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/09/Strawberry-ice-mango-peach-watermelon.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Strawberry Kiwi + Strawberry Raspberry Cherry Ice",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/09/Strawberry-kiwi-Strawberryraspberry-chery-ice.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Strawberry Raspberry Cherry Ice + Grape Ice",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/strawberry-raspberry-cherry-ice-grape-ice-1-600x600.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Strawberry Watermelon + Gummy Bear",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/Strawberry-Watermelon-Gummy-Bear-600x600.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Triple Melon + Pineapple Coconut",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/09/triple-melon-Pineapple-coconut.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Triple Melon + Raspberry Watermelon",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/09/triple-melon-raspberry-watermelon.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Watermelon Ice + Mixed Berry",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/watermelon-ice-mixed-berry-1-600x600.png"
        ),
        ProductoBase(
            tipo="Twins",
            nombre="Watermelon Ice + Strawberry Mango",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/watermelon-ice-strawberry-mango-1-600x600.png"
        ),





        #VIKING
        ProductoBase(
            tipo="Viking",
            nombre="Blueberry",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/blueberry-ice-600x600.png"
        ),
        ProductoBase(
            tipo="Viking",
            nombre="Blueberry Cherry Cranberry",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/blueberry-cherry-cranberry-600x600.png"
        ),
        ProductoBase(
            tipo="Viking",
            nombre="Blueberry Raspberry",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/blueberry-raspberry-600x600.png"
        ),
        ProductoBase(
            tipo="Viking",
            nombre="Fizzy Cherry",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/fizzy-cherry-600x600.png"
        ),
        ProductoBase(
            tipo="Viking",
            nombre="Fresh Mint",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/11/fresh-mint-600x600.png"
        ),
        ProductoBase(
            tipo="Viking",
            nombre="Gummy Bear",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/gummy-bear-600x600.png"
        ),
        ProductoBase(
            tipo="Viking",
            nombre="Lemon Lime",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/lemon-lime-600x600.png"
        ),
        ProductoBase(
            tipo="Viking",
            nombre="Lemon Peach",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/lemon-peach-600x600.png"
        ),
        ProductoBase(
            tipo="Viking",
            nombre="Red Apple Ice",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/red-apple-ice-600x600.png"
        ),
        ProductoBase(
            tipo="Viking",
            nombre="Strawberry Banana",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/strawberry-banana-600x600.png"
        ),
        ProductoBase(
            tipo="Viking",
            nombre="Strawberry Kiwi",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/strawberry-kiwi-600x600.png"
        ),
        ProductoBase(
            tipo="Viking",
            nombre="Strawberry Raspberry Ice",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/strawberry-raspberry-ice-600x600.png"
        ),
        ProductoBase(
            tipo="Viking",
            nombre="Strawberry Watermelon",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/strawberry-watermelon-600x600.png"
        ),
        ProductoBase(
            tipo="Viking",
            nombre="Summer Dream",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/summer-dream-600x600.png"
        ),
        ProductoBase(
            tipo="Viking",
            nombre="Watermelon Ice",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/watermelon-ice-600x600.png"
        ),
    ]

    db.session.bulk_save_objects(productos)
    db.session.commit()
    print(f"{len(productos)} productos base añadidos correctamente.")
