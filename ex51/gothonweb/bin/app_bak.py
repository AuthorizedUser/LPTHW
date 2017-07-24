import web

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index:
    def GET(self):
        greeting = "Hello World"
        return render.foo(greeting = greeting)

if __name__ == "__main__":
    app.run()
