from flask import Flask, request, jsonify
from database import db
from models.food import Food

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/daily-diet'

db.init_app(app)

#Registra o alimento
@app.route("/refeicao", methods=["POST"])
def ref_register():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    date = data.get("date")
    hour = data.get("hour")
    diet = data.get("diet")

    if name and description and date and hour and diet:
        food = Food(name=name, description=description, date=date, hour=hour, diet=diet)
        db.session.add(food)
        db.session.commit()
        return jsonify({"message": "Refeição adiciona com sucesso!"})
    return jsonify({"message": "Não foi possivel concluir o registro da refeição!"}), 400

#Edita o que achar necessário na refeição
@app.route("/refeicao/<int:id>", methods=["PUT"])
def update_food(id):
    data = request.json
    food = Food.query.get(id)
    if food:
        food.name = data.get("name")
        food.description = data.get("description")
        food.date = data.get("date")
        food.hour = data.get("hour")
        food.diet = data.get("diet")
        db.session.commit()
        return jsonify({"message": "Os dados da refeição foram atualizados com sucesso!"})
    return jsonify({"message", "Refeição não encontrada"}), 404

#Deleta a refeição informada
@app.route("/refeicao/<int:id>", methods=["DELETE"])
def delete_food(id):
    food = Food.query.get(id)

    if food:
        db.session.delete(food)
        db.session.commit()
        return jsonify({"message": "Refeição deletada com sucesso!"})
    return jsonify({"message": "Refeição não encontrada"}), 404

#Lista as refeições
@app.route("/refeicao", methods=["GET"])
def read_foods():
    food = Food.query.all()
    refeicoes = []
    print(f"Temos um total de {len(food)} refeições!")
    for i in food:
        refeicoes.append({
            "name": i.name,
            "description": i.description,
            "date": i.date,
            "hour": i.hour,
            "diet": i.diet
    })
    return jsonify(refeicoes)
    
    
#Lista refeição especifica
@app.route("/refeicao/<int:id>", methods=["GET"])
def read_food(id):
    food = Food.query.get(id)
    if food:
        return{
                "name": food.name,
                "description": food.description,
                "date": food.date,
                "hour": food.hour,
                "diet": food.diet
            }
    return jsonify({"message": "Refeição não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)