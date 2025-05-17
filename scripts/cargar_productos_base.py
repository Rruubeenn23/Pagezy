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
            tipo="Vaper",
            categoria="Super",
            nombre="Black Ice DragonFruit Strawberry",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/BLACK-ICE-DRAGONFRUIT-STRAWBERRY-600x600.png"
        ),ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Blue Razz",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/BLUE-RAZZ-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Blueberry Blackcurrant Ice",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/02/blueberry-blackcurrant-ice-2-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Blueberry Cherry Cola",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/BLUEBERRYCHERRY-COLA-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Blueberry Cherry Cranberry",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/BLUEBERRY-CHERRY-CRANBERRY-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Blueberry Ice",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/BLUEBERRY-ICE-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Double Apple",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/DOUBLE-APPLE-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Lemon Lime",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/LEMON-LIME-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Mixed Berry",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/MIXED-BERRY-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Peach Mango Pineapple",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/02/peach-mango-pineapple-1-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Pink Lemonade",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/02/pink-lemonade-1-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Raspberry Watermelon",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/RASPBERRY-WATERMELON-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Red Bull",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/RED-BULL-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Skittles",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/SKITTLES-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Strawberry Banana",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/STRAWBERRY-BANANA-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Strawberry Ice",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/02/strawberry-ice-1-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Strawberry Kiwi",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/STRAWBER-KIWI-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Strawberry Vainilla Cola",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/02/strawberry-vanilla-cola-1-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Red Bull",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/SUMMER-DREAM-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Super",
            nombre="Watermelon Ice",
            caladas=15000,
            precio=12.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/SUMMER-DREAM-600x600.png"
        ),





        #GALAXY
        ProductoBase(
            tipo="Vaper",
            categoria="Galaxy",
            nombre="Black Ice DragonFruit Strawberry",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/6BLACKICEDRAGONFRUITSTRAWBERRY%E9%BB%91%E5%86%B0%E7%81%AB%E9%BE%99%E6%9E%9C%E8%8D%89%E8%8E%93.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Galaxy", 
            nombre="Blue Razz",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/2BLUERAZZ%E8%93%9D%E8%8E%93%E6%8B%89%E5%85%B9.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Galaxy", 
            nombre="Lemon Lime",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/5LEMONLIME%E6%9F%A0%E6%AA%AC%E9%9D%92%E6%9F%A0.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Galaxy", 
            nombre="Lemon Peach",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/7LEMONPEACH%E6%9F%A0%E6%AA%AC%E6%A1%83%E5%AD%90.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Galaxy", 
            nombre="Pineapple Coconut",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/3PINEAPPLECOCONUT%E8%8F%A0%E8%90%9D%E6%A4%B0%E5%AD%90.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Galaxy", 
            nombre="Raspberry Watermelon",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/1RASPBERRYWATERMELON%E6%A0%91%E8%8E%93%E8%A5%BF%E7%93%9C.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Galaxy", 
            nombre="Strawberry Banana",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/11STRAWBERRYBANANA%E8%8D%89%E8%8E%93%E9%A6%99%E8%95%89.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Galaxy", 
            nombre="Strawberry Kiwi",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/9STRAWBERRYKIWI%E8%8D%89%E8%8E%93%E5%A5%87%E5%BC%82%E6%9E%9C.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Galaxy", 
            nombre="Strawberry Raspberry Cherry Ice",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/8STRAWBERRYRASPBERRYCHERRYICE%E8%8D%89%E8%8E%93%E6%A0%91%E8%8E%93%E6%A8%B1%E6%A1%83%E5%86%B0.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Galaxy", 
            nombre="Strawberry Red Bull",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/10STRAWBERRYREDBULL%E8%8D%89%E8%8E%93%E7%BA%A2%E7%89%9B.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Galaxy", 
            nombre="Triple Melon",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/12TRIPLEMELON%E4%B8%89%E9%87%8D%E8%9C%9C%E7%93%9C.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Galaxy", 
            nombre="Watermelon Ice",
            caladas=30000,
            precio=18.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/4WATERMELONICE%E8%A5%BF%E7%93%9C%E5%86%B0.png"
        ),




        #TRIPLE
        ProductoBase(
            tipo="Vaper",
            categoria="Triple", 
            nombre="BlackCurrant Ice + Pink Lemonade + Kiwi Passion Fruit Guava",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/blackcurrant-ice-pink-lemonade-kiwi-passion-fruit-guava-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Triple",
            nombre="Blueberry Sour Raspberry + Strawberry Mango + Lemon Cola",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/Bluberry-soue-rasberry-strawberry-mango-lemon-cola-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Triple",
            nombre="Kiwi Passion Fruit + Love 66 + Vanilla",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/Kiwi-passions-fruit-Love-66-Vanilla-1-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Triple",
            nombre="Lemon Lime `Strawberry Watermelon + Blueberry Ice",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/LEMON-LIME-STRAWBERRY-WATERMELON-BLUEBERRY-ICE-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Triple",
            nombre="Peach Berry + Black Ice + Strawberry Vanilla Cola",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/peach-berry-black-ice-starwberry-vanilla-cola-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Triple",
            nombre="Peach Ice + Dragon Fruit Ice + Mix Fruit",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/Peach-ice-dragon-fruit-ice-mix-fruit-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Triple",
            nombre="Pineapple Coconut + Strawberry Banana + Blue Razz",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/PINEAPPLE-COCONUT-STRAWBERRY-BANANA-BLUE-R-AZZ-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Triple",
            nombre="Raspberry Watermelon + Mango Peach + Strawberry Kiwi",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/RASPBERRY-WATERMELON-MANGO-PEACH-STRAWBERRY-KIWI-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Triple",
            nombre="Strawberry Banana ` Raspberry Watermelon + Lemon Lime",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/STRAWBERRY-BANANA-RASPBERRY-WATERMELON-LEMON-LIME-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Triple",
            nombre="Strawberry Kiwi + Sour Mango Pineapple + Red Bull",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/STRAWBERRY-KIWI-SOUR-MANGO-PINEAPPLE-RED-BULL-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Triple",
            nombre="Strawberry Raspberry + Triple Melon + Sour Mango Pineapple",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/STRAWBERRY-RASPBERRY-TRIPLE-MELON-SOUR-MANGO-PINEAPPLE-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Triple",
            nombre="Strawberry Vanilla Coke + Blueberry Raspberry + Lemon Lime",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/STRAWBERRY-VANILLA-COKE-BLUEBERRY-RASPBERRY-LEMON-LIME-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Triple",
            nombre="Tropical Fruit + Strawberry Watermelon + Lemon Peach",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/TROPICAL-FRUIT-STRAWBERRY-WATERMELON-LEMON-PEACH-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Triple",
            nombre="Watermelon Ice + Red Bull + Strawberry Kiwi",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/WATERMELON-ICE-RED-BULL-STRAWBERRY-KIWI-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Triple",
            nombre="Watermelon Ice + Strawberry Ice Cream + Triple Melon",
            caladas=30000,
            precio=19.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/12/WATERMELON-ICE-STRAWBERRY-ICECREAM-TRIPLE-MELON-600x600.png"
        ),


        #TWINS
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Black Ice Dragon Fruit Strawberry + Raspberry Watermelon",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/09/Black-ice-dragon-fruit-strawberry-Raspberry-watermelon.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Blue Razz Lemonade + Lemon Lime",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/blue-razz-lemonadelemon-lime-2-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Blueberry Blackcurrant + GrapeFruit Refresher",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/Blueberry-Blackurrant-Grapefruit-Refresher-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Blueberry Ice + Fizzy Cherry",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/blueberry-ice-fizzy-cherry-1-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Cherry Cola + Juicy Peach Ice",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/Cherry-Cola-Juicy-Peach-Ice-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Grape Ice + Strawberry Kiwi",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/grape-ice-strawberry-kiwi-1-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Lemon Lime + Watermelon Ice",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/lemon-lime-watermelon-1-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Orange mango Watermelon + Red Bull",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/orange-mango-watermelon-redbull-1-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Passion Fruit Mojito + Triple Mint",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/Passion-Fruit-Mojito-Triple-Mint-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Pineapple Coconut + Strawberry Banana",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/pineapple-coconut-strawberry-banana-1-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Pineapple Coconut + Watermelon Ice",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/09/Pineapple-coconut-watermelon-ice.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Strawberry Banana + Fizzy Cherry",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/STRAWBERRY-BANANAFIZZY-CHERRY1-1-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Strawberry Ice + Mango Peach Watermelon",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/09/Strawberry-ice-mango-peach-watermelon.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Strawberry Kiwi + Strawberry Raspberry Cherry Ice",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/09/Strawberry-kiwi-Strawberryraspberry-chery-ice.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Strawberry Raspberry Cherry Ice + Grape Ice",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/strawberry-raspberry-cherry-ice-grape-ice-1-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Strawberry Watermelon + Gummy Bear",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2025/03/Strawberry-Watermelon-Gummy-Bear-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Triple Melon + Pineapple Coconut",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/09/triple-melon-Pineapple-coconut.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Triple Melon + Raspberry Watermelon",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/09/triple-melon-raspberry-watermelon.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Watermelon Ice + Mixed Berry",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/watermelon-ice-mixed-berry-1-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Twins",
            nombre="Watermelon Ice + Strawberry Mango",
            caladas=20000,
            precio=16.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/06/watermelon-ice-strawberry-mango-1-600x600.png"
        ),


        #VIKING
        ProductoBase(
            tipo="Vaper",
            categoria="Viking",
            nombre="Blueberry",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/blueberry-ice-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Viking",
            nombre="Blueberry Cherry Cranberry",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/blueberry-cherry-cranberry-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Viking",
            nombre="Blueberry Raspberry",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/blueberry-raspberry-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Viking",
            nombre="Fizzy Cherry",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/fizzy-cherry-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Viking",
            nombre="Fresh Mint",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/11/fresh-mint-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Viking",
            nombre="Gummy Bear",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/gummy-bear-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Viking",
            nombre="Lemon Lime",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/lemon-lime-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Viking",
            nombre="Lemon Peach",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/lemon-peach-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Viking",
            nombre="Red Apple Ice",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/red-apple-ice-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Viking",
            nombre="Strawberry Banana",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/strawberry-banana-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Viking",
            nombre="Strawberry Kiwi",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/strawberry-kiwi-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Viking",
            nombre="Strawberry Raspberry Ice",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/strawberry-raspberry-ice-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Viking",
            nombre="Strawberry Watermelon",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/strawberry-watermelon-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Viking",
            nombre="Summer Dream",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/summer-dream-600x600.png"
        ),
        ProductoBase(
            tipo="Vaper",
            categoria="Viking",
            nombre="Watermelon Ice",
            caladas=12000,
            precio=9.99,
            imagen_url="https://static.vapsolo.com/uploads/sites/3/2024/02/watermelon-ice-600x600.png"
        ),



        # ROPA

        # OG'S
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="True Felino - Relaxed fit T-Shirt",
            precio=34.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/LEGENDS_OGS_Black_Shirt_Front.2e16d0ba.fill-800x933-c100.png"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="True Felino - Oversized Hoddie",
            precio=59.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/LEGENDS_OGS_Black_Hoodie_Fron.2e16d0ba.fill-800x933-c100.png"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="PARANOIA - Camiseta Relaxed Fit",
            precio=34.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/PARANOIA_White_RELAX_TEE_FRON.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="PARANOIA - Relaxed Fit T-Shirt",
            precio=34.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/PARANOIA_Black_RELAX_TEE_FRON.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="PARANOIA - Hoodie Oversized",
            precio=59.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/PARANOIA_White_HOODIE_PREMIUM.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="PARANOIA - Hoodie Oversized",
            precio=59.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/PARANOIA_Black_HOODIE_PREMIUM.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="KLVR - Camiseta Relaxed Fit",
            precio=34.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/KLVR_White_RELAX_TEE_BACK.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="KLVR - Camiseta Relaxed Fit",
            precio=34.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/KLVR_Black_RELAX_TEE_FRONT.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="KLVR - Oversized Hoodie",
            precio=59.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/KLVR_White_HOODIE_PREMIUM_BAC.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="KLVR - Oversized Hoodie",
            precio=59.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/KLVR_Black_HOODIE_PREMIUM_FRO.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="THE LOVERS - Huge Oversized Tee",
            precio=34.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/OGS_SUMMER23_Lovers_CamisetaH.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="THE LOVERS - Huge Oversized Tee",
            precio=34.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/Copia_de_OGS_SUMMER23_Lovers_.2e16d0ba.fill-800x933-c100_EdeowE7.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="CLASSY - Hoodie Oversized",
            precio=59.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/Copy_of_OGS_BTS2023_Classic_H.2e16d0ba.fill-800x933-c100_xysIItz.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="OG's - Camiseta",
            precio=34.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/OGS_Originals_Camiseta_AzulCi.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="The OG's - Crewneck",
            precio=49.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/OGS_Originals_Crewneck_Black_.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="OG's - Hoodie",
            precio=59.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/OGS_Originals_Hoodie_Burgundy.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="KIR - Gorra",
            precio=24.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/DSC_0526.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="OG's Bucket (Reversible)",
            precio=24.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/DSC_0531.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="SOGS",
            precio=24.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/OGS_SOGS_3.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="SKULLRAMEN - Hoodie",
            precio=59.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/Copy_of_OGS_BTS2023_SKULLRAME.2e16d0ba.fill-800x933-c100_byKlnzE.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="FEELING YOUNG - Hoodie",
            precio=59.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/OGS_FEB24_FeelingYoung_Hoodie.2e16d0ba.fill-800x933-c100_QLqWdcx.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="SKULLRAMEN - Camiseta",
            precio=34.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/OGS_NOV23_LosOGS_Camiseta_Bla.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="FEELING YOUNG - Camiseta",
            precio=34.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/OGS_FEB24_FeelingYoung_TShirt.2e16d0ba.fill-800x933-c100_LWDs5A9.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="FATALITY - Hoodie",
            precio=59.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/Copy_of_OGS_BTS2023_FATALITY2.2e16d0ba.fill-800x933-c100_Yj2nbuY.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="ALFRED - Hoodie",
            precio=59.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/Copy_of_OGS_BTS2023_HITCHCOCK.2e16d0ba.fill-800x933-c100_wD7OQxv.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="FATALITY - Camiseta",
            precio=34.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/Copy_of_OGS_BTS2023_FATALITY2.2e16d0ba.fill-800x933-c100_boLozRh.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="OG's",
            nombre="ALFRED - Camiseta",
            precio=34.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/Copy_of_OGS_BTS2023_HITCHCOCK.2e16d0ba.fill-800x933-c100_CWFwqbg.jpg"
        ),




        ProductoBase(
            tipo="Ropa",
            categoria="MadKat",
            nombre="Loves me, loves me not - Camiseta Relaxed Fit",
            precio=34.99,
            imagen_url="https://leeos-merch.storage.googleapis.com/media/images/MADKAT_SPRING2024_FlowerMadne.2e16d0ba.fill-800x933-c100_Wz2q5MS.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="MadKat",
            nombre="Loves me, loves me not - Hoodie",
            precio=59.99,
            imagen_url="https://leeos-merch.storage.googleapis.com/media/images/MADKAT_SPRING2024_FlowerMadne.2e16d0ba.fill-800x933-c100_ry0IDpY.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="MadKat",
            nombre="Mr. Kat - Camiseta Relax Fit",
            precio=34.99,
            imagen_url="https://leeos-merch.storage.googleapis.com/media/images/MADKAT_SPRING2024_MrKat_TShir.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="MadKat",
            nombre="Mr. Kat - Camiseta Relax Fit",
            precio=34.99,
            imagen_url="https://leeos-merch.storage.googleapis.com/media/images/MADKAT_SPRING2024_MrKat_TShir.2e16d0ba.fill-800x933-c100_KVVU5yL.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="MadKat",
            nombre="Mr. Kat - Hoodie",
            precio=59.99,
            imagen_url="https://leeos-merch.storage.googleapis.com/media/images/MADKAT_SPRING2024_MrKat_Hoodi.2e16d0ba.fill-800x933-c100_pf3mRT5.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="MadKat",
            nombre="Mr. Kat - Hoodie",
            precio=59.99,
            imagen_url="https://leeos-merch.storage.googleapis.com/media/images/MADKAT_SPRING2024_MrKat_Hoodi.2e16d0ba.fill-800x933-c100_3fv9eHc.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="MadKat",
            nombre="MadKat Worldtour - Camiseta",
            precio=34.99,
            imagen_url="https://leeos-merch.storage.googleapis.com/media/images/02_A_MADKAT_Camiseta_Creator_.2e16d0ba.fill-800x933-c100_fqS4qkB.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="MadKat",
            nombre="Scratching Worldwide - Camiseta Relaxed Fit",
            precio=34.99,
            imagen_url="https://leeos-merch.storage.googleapis.com/media/images/03_A_MADKAT_Camiseta_Relax_Te.2e16d0ba.fill-800x933-c100_IQF88mU.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="MadKat",
            nombre="ALFRED - Camiseta",
            precio=34.99,
            imagen_url="https://ogsbrand.storage.googleapis.com/media/images/Copy_of_OGS_BTS2023_HITCHCOCK.2e16d0ba.fill-800x933-c100_CWFwqbg.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="MadKat",
            nombre="Originals - Camiseta",
            precio=34.99,
            imagen_url="https://leeos-merch.storage.googleapis.com/media/images/17.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="MadKat",
            nombre="Originals - Camiseta",
            precio=34.99,
            imagen_url="https://leeos-merch.storage.googleapis.com/media/images/9._CAMISETA_ORIGINALS_ROSA_LO.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="MadKat",
            nombre="New Originals - Camiseta",
            precio=34.99,
            imagen_url="https://leeos-merch.storage.googleapis.com/media/images/NewOriginals_grande_Camiseta_.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="MadKat",
            nombre="New Originals - Hoodie",
            precio=59.99,
            imagen_url="https://leeos-merch.storage.googleapis.com/media/images/MadKat_BTS22_SIMPLIFICADOX_Su.2e16d0ba.fill-800x933-c100_3LOh4Yf.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="MadKat",
            nombre="Beanies + Pins pack Clashing Boldness",
            precio=24.99,
            imagen_url="https://leeos-merch.storage.googleapis.com/media/images/MADKAT_Beanie_PurpleOrange_Pi.2e16d0ba.fill-800x933-c100.jpg"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="MadKat",
            nombre="Originals - Gorra",
            precio=24.99,
            imagen_url="https://leeos-merch.storage.googleapis.com/media/images/MKUB22_01.2e16d0ba.fill-800x933-c100.jpg"
        ),


        # M***SHAKES
        ProductoBase(
            tipo="Ropa",
            categoria="M***SHAKES",
            nombre="π Shirt",
            precio=18.69,
            imagen_url="https://milfshakes.es/cdn/shop/files/Numeropitee_d6dae41a-bf1c-4904-a9dc-3e709f5bf1fa.png?v=1746446201"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="M***SHAKES",
            nombre="*** TRACKSUIT",
            precio=99.99,
            imagen_url="https://milfshakes.es/cdn/shop/files/WhatsApp_Image_2025-04-18_at_16.53.43.jpg?v=1745765154"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="M***SHAKES",
            nombre="MLFSHKS CAP",
            precio=29.69,
            imagen_url="https://milfshakes.es/cdn/shop/files/lateral.png?v=1745764983"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="M***SHAKES",
            nombre="BUILD TEE",
            precio=34.69,
            imagen_url="https://milfshakes.es/cdn/shop/files/680e408fd5669851b0942815_BACKSINFONDO.resized.webp?v=1745765333"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="M***SHAKES",
            nombre="SEEKING TEE",
            precio=34.69,
            imagen_url="https://milfshakes.es/cdn/shop/files/seeking_back.webp?v=1738500114"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="M***SHAKES",
            nombre="TOAST TEE",
            precio=34.69,
            imagen_url="https://milfshakes.es/cdn/shop/files/TOSTADA-TEE-MOCKUP-BACK.webp?v=1738503265"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="M***SHAKES",
            nombre="MILF LOVER TEE",
            precio=34.69,
            imagen_url="https://milfshakes.es/cdn/shop/files/680793e7c9e6537910a310a1_Lover_Tee_back.webp?v=1745327483"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="M***SHAKES",
            nombre="CAUTION TEE",
            precio=34.69,
            imagen_url="https://milfshakes.es/cdn/shop/files/680e408f1cee1884a2b6b0c1_ALERT-TEE-MOCKUP-FRONT.resized.webp?v=1745765391"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="M***SHAKES",
            nombre="ALIEN HOODIE",
            precio=59.69,
            imagen_url="https://milfshakes.es/cdn/shop/files/680e40af3f679ef5a18df7a8_ALIEN-HOODIE-MOCKUP-BACK.resized.webp?v=1745765505"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="M***SHAKES",
            nombre="HOODIE VICIO x MILFSHAKES",
            precio=59.69,
            imagen_url="https://milfshakes.es/cdn/shop/files/680e40530996393aaf3266d2_hoodie-back1_d3b46a59-82fb-4a1d-b63b-6de66601c25f.webp?v=1745765524"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="M***SHAKES",
            nombre="ELECTRIC ZIPPER HOODIE",
            precio=59.69,
            imagen_url="https://milfshakes.es/cdn/shop/files/ZIPHOODIEBACK.webp?v=1738491444"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="M***SHAKES",
            nombre="FOLDED TEE WHITE",
            precio=34.69,
            imagen_url="https://milfshakes.es/cdn/shop/files/680793e2269b1ce0867b17c0_Folded_white_tee.webp?v=1745327587"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="M***SHAKES",
            nombre="GUN TEE WHITE",
            precio=34.69,
            imagen_url="https://milfshakes.es/cdn/shop/files/680e40c91cee1884a2b6ca82_BACK-BLANCA-PM.webp?v=1745765311"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="M***SHAKES",
            nombre="ASTERISK KNIT - GREY",
            precio=59.69,
            imagen_url="https://milfshakes.es/cdn/shop/files/680e40af9bf5c7568967bd2b_tricot-black_1x1.resized.webp?v=1745765022"
        ),
        ProductoBase(
            tipo="Ropa",
            categoria="M***SHAKES",
            nombre="FLOWER HOODIE",
            precio=59.69,
            imagen_url="https://milfshakes.es/cdn/shop/files/BACKSINFONDO_11b22c52-9229-4650-9557-93bef23425b7.webp?v=1738458940"
        ),

        # VIDEOJUEGOS

        #PS5
        ProductoBase(
            tipo="Videojuegos",
            categoria="PS5",
            nombre="Forza Horizon 5 Standart Edition",
            precio=79.99,
            imagen_url="https://image.api.playstation.com/vulcan/ap/rnd/202501/2717/42b3ee6b1b2094212231b0b0a82824f687fc5c4dc9bde31c.png?w=230&thumb=false"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="PS5",
            nombre="DOOM: The Dark Ages",
            precio=79.99,
            imagen_url="https://image.api.playstation.com/vulcan/ap/rnd/202501/1405/346673e154a94c7d1dba15de4040b8f148dd3aafda800100.png?w=230&thumb=false"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="PS5",
            nombre="The Elder Scrolls IV: Oblivion Remastered",
            precio=79.99,
            imagen_url="https://image.api.playstation.com/vulcan/ap/rnd/202504/0320/dda6507cae2232eed3e7ab82a5a3acddd7dcf182458658d7.png?w=230&thumb=false"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="PS5",
            nombre="The Last of Us Parte II Remastered",
            precio=79.99,
            imagen_url="https://image.api.playstation.com/vulcan/ap/rnd/202311/1717/0124532002d9b1295418e44465ceb3d3e9c1718416800efb.png?w=230&thumb=false"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="PS5",
            nombre="Days Gone Remastered",
            precio=79.99,
            imagen_url="https://image.api.playstation.com/vulcan/ap/rnd/202502/1302/101e46bff876389c0b12a5bdf72328ecd03c391979791ef2.png?w=230&thumb=false"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="PS5",
            nombre="Resident Evil 4",
            precio=79.99,
            imagen_url="https://image.api.playstation.com/vulcan/ap/rnd/202210/0706/EVWyZD63pahuh95eKloFaJuC.png?w=230&thumb=false"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="PS5",
            nombre="Marvel's Spider-Man 2",
            precio=79.99,
            imagen_url="https://image.api.playstation.com/vulcan/ap/rnd/202306/1219/1c7b75d8ed9271516546560d219ad0b22ee0a263b4537bd8.png?w=230&thumb=false"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="PS5",
            nombre="Baldur's Gate 3",
            precio=79.99,
            imagen_url="https://image.api.playstation.com/vulcan/ap/rnd/202302/2321/ba706e54d68d10a0eb6ab7c36cdad9178c58b7fb7bb03d28.png?w=230&thumb=false"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="PS5",
            nombre="ASTRO BOT",
            precio=79.99,
            imagen_url="https://image.api.playstation.com/vulcan/ap/rnd/202406/0500/8f15268257b878597757fcc5f2c9545840867bc71fc863b1.png?w=230&thumb=false"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="PS5",
            nombre="Avatar: Frontiers of Pandora",
            precio=79.99,
            imagen_url="https://image.api.playstation.com/vulcan/ap/rnd/202306/0113/38ad0cc5b92af440d46ccebf5d1f271213d656684fce3385.png?w=180&thumb=false"
        ),

        #XBOX
        ProductoBase(
            tipo="Videojuegos",
            categoria="XBOX Series",
            nombre="Call of Duty: Black Ops 6",
            precio=79.99,
            imagen_url="https://store-images.s-microsoft.com/image/apps.37927.14207097610490811.5b338e31-5c12-4d95-9a2a-2f16ceb01377.52b31dce-5e51-4f9f-88c3-9f40367f021f?q=90&w=177&h=265"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="XBOX Series",
            nombre="NBA 2K25",
            precio=79.99,
            imagen_url="https://store-images.s-microsoft.com/image/apps.17984.14250775457519092.f33de21f-07ee-4aaf-a0c4-413615c9c9f0.e0fa7993-a5bd-4036-a403-6db666315d8b?q=90&w=177&h=265"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="XBOX Series",
            nombre="EA SPORTS FC 25",
            precio=79.99,
            imagen_url="https://store-images.s-microsoft.com/image/apps.39617.13862251612333050.ec09080a-b13c-432f-96c1-4c1d38bfef9c.b0deca43-6ba3-4ec9-9013-4b1b0763011d?q=90&w=177&h=265"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="XBOX Series",
            nombre="Red Dead Redemption 2",
            precio=79.99,
            imagen_url="https://store-images.s-microsoft.com/image/apps.34695.13942869738016799.078aba97-2f28-440f-97b6-b852e1af307a.b278e12f-c22c-4a2a-bb18-dfd26ca6cafc?q=90&w=177&h=265"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="XBOX Series",
            nombre="Split Fiction",
            precio=79.99,
            imagen_url="https://store-images.s-microsoft.com/image/apps.27923.13967700947391483.c0292e51-6aa2-4293-9562-d6330dc0d37b.c206d39f-d075-4a9e-a007-566d9fe521ed?q=90&w=177&h=265"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="XBOX Series",
            nombre="Mortal Kombat 1",
            precio=79.99,
            imagen_url="https://store-images.s-microsoft.com/image/apps.19049.14510046067132622.b911a928-b45b-4314-a33a-67964f2dbf45.d6710f28-7394-4de2-b286-0df084812038?q=90&w=177&h=265"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="XBOX Series",
            nombre="ARK: Survival Ascended",
            precio=79.99,
            imagen_url="https://store-images.s-microsoft.com/image/apps.47381.14545480955348978.f72b621c-2a7f-403c-8bd4-126f7310ad33.c2cc3983-f689-401d-9deb-e46cb33271be?q=90&w=177&h=265"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="XBOX Series",
            nombre="ELDEN RING",
            precio=79.99,
            imagen_url="https://store-images.s-microsoft.com/image/apps.25322.14537704372270848.6ecb6038-5426-409a-8660-158d1eb64fb0.d230176a-d7a2-4696-ad23-ff53a6e004df?q=90&w=177&h=265"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="XBOX Series",
            nombre="Raft",
            precio=79.99,
            imagen_url="https://store-images.s-microsoft.com/image/apps.32463.14102062639781722.573266e7-686b-44fb-9e48-a2585bc2170f.5424f649-5154-402f-88e5-905dae685f22?q=90&w=177&h=265"
        ),
        ProductoBase(
            tipo="Videojuegos",
            categoria="XBOX Series",
            nombre="Subnautica",
            precio=79.99,
            imagen_url="https://store-images.s-microsoft.com/image/apps.24838.63409341877910445.4fd452e1-c3ee-4448-a0f8-ac6eb6bdaabf.d531d87c-d1b7-497f-b802-baabfb728090?q=90&w=177&h=265"
        ),
        
    ]

    db.session.bulk_save_objects(productos)
    db.session.commit()
    print(f"{len(productos)} productos base añadidos correctamente.")
