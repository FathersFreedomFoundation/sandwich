from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def make_turkey_sandwich():
    # Step 1: Gather Ingredients
    ingredients = {
        "bread": "rye bread",
        "mayo": "mayonnaise",
        "mustard": "German mustard",
        "lettuce": "lettuce",
        "tomato": "tomato",
        "cheese": "Provolone cheese",
        "turkey": "turkey slices"
    }
    
    # Step 2: Prepare Ingredients
    def prepare_ingredients(ingredients):
        ingredients["lettuce"] = "washed lettuce"
        ingredients["tomato"] = "sliced tomato"
        return ingredients

    prepared_ingredients = prepare_ingredients(ingredients)
    
    # Step 3: Assemble Sandwich
    def assemble_sandwich(ingredients):
        sandwich = []
        sandwich.append(f"1 slice of {ingredients['bread']}")
        sandwich.append(f"Spread {ingredients['mayo']} on one slice")
        sandwich.append(f"Spread {ingredients['mustard']} on the other slice")
        sandwich.append(f"Add {ingredients['cheese']}")
        sandwich.append(f"Add {ingredients['turkey']}")
        sandwich.append(f"Add {ingredients['lettuce']}")
        sandwich.append(f"Add {ingredients['tomato']}")
        sandwich.append(f"Top with another slice of {ingredients['bread']}")
        return sandwich

    sandwich = assemble_sandwich(prepared_ingredients)
    
    # Step 4: Serve Sandwich
    def serve_sandwich(sandwich):
        result = "Your sandwich is ready:<br>"
        for step in sandwich:
            result += step + "<br>"
        result += "Cut the sandwich in half (optional)<br>"
        result += "Serve on a plate"
        return result

    result = serve_sandwich(sandwich)
    
    # HTML Template with Styles
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Turkey Sandwich</title>
        <style>
            body {
                background-color: black;
                color: blue;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div>
            <h1>{{ result|safe }}</h1>
        </div>
    </body>
    </html>
    """

    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

