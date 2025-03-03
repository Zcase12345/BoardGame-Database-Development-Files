from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import BoardGame, db

boardgames = Blueprint('boardgames', __name__)

# Lets New Games Be Put In
@boardgames.route('/add-game', methods=['GET', 'POST'])
@login_required
def add_game():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        image = request.form.get('image')

        new_game = BoardGame(name=name, description=description, image=image)
        db.session.add(new_game)
        db.session.commit()
        flash('Board game added!', category='success')
        return redirect(url_for('views.home'))

    return render_template('add_game.html', user=current_user)

# View All Board Games
@boardgames.route('/games')
@login_required
def view_games():
    games = BoardGame.query.all()
    return render_template('view_games.html', user=current_user, games=games)

# Edit a Board Game
@boardgames.route('/edit-game/<int:game_id>', methods=['GET', 'POST'])
@login_required
def edit_game(game_id):
    game = BoardGame.query.get_or_404(game_id)
    if request.method == 'POST':
        game.name = request.form.get('name')
        game.description = request.form.get('description')
        game.image = request.form.get('image')

        db.session.commit()
        flash('Board game updated!', category='success')
        return redirect(url_for('boardgames.view_games'))

    return render_template('edit_game.html', user=current_user, game=game)

# Delete a Board Game
@boardgames.route('/delete-game/<int:game_id>', methods=['POST'])
@login_required
def delete_game(game_id):
    game = BoardGame.query.get_or_404(game_id)
    db.session.delete(game)
    db.session.commit()
    flash('Board game deleted', category='success')
    return redirect(url_for('boardgames.view_games'))
