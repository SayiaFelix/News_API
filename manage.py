# from app import create_app
# from flask_script import Manager,Server

# # Creating app instance
# app = create_app('development')

# manager = Manager(app)
# manager.add_command('server',Server)

# @manager.command

# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

from app import app

if __name__ == '__main__':
    app.run(debug = True)



# if __name__ == '__main__':
#     app.run()     