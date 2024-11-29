from odoo import fields, models

class Movie(models.Model):
    _name = "proyectorium.movie"
    _description = "stores all the movies"

    # simple fields
    title = fields.Char(string="Movie name", required = True)
    sinopsis = fields.Text(string="Movie sinopsis")
    duration = fields.Integer(integer= "Movie duration")
    release_date = fields.Date(string = "Release date")
    movie_hour = fields.Selection(
        selection=[
            ('16:00', '16:00'),
            ('18:00', '18:00'),
            ('20:00', '20:00'),
            ('22:00', '22:00'),
        ],
        string="Movie Hour",
        required=True,
        help="The hour slot for the movie screening",
    )