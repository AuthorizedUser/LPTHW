import web

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index:
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(greet=None, name="Nobody")
        greeting = "Hello, %s, %s" % (form.name, form.greet)
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
