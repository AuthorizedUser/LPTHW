import web
from gothonweb import map

urls = (
    '/game', 'GameEngine',
    '/', 'Index',
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None: #start a new session is _session is blank?
    store = web.session.DiskStore('sessions') #begin storing in sessions
    session = web.session.Session(app, store, #session instance
                                 initializer={'room': None})
    web.config._session = session #stores the session in _session
else:
    session = web.config._session #existing session

render = web.template.render('templates/', base="layout")
# render object uses the layout base in templates folder


class Index(object):
    def GET(self):
        # this is used to 'setup' the session with starting values
        session.room = map.START #sets the aforementioned room initializer
        web.seeother("/game") #is it a function that changes url end to /game?


class GameEngine(object):

    def GET(self):
        if session.room: #if session.room has been populated
            return render.show_room(room=session.room) # new template
        else:
            # why is there here? do you need it?
            return render.you_died() # new function

    def POST(self):
        form = web.input(action=None)

        # there is a bug here, can you fix it?
        if form.action in session.room.paths: #fixed from 'and'
        # so if the room name is entered in input... it calls go
            session.room = session.room.go(form.action)

        web.seeother("/game")

if __name__ == "__main__":
    app.run()
