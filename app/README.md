# [MVC Architecture](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)

## [MVC Models](./models)

> The central component of the pattern. It is the application's dynamic data structure, independent of the user interface. It directly manages the data, logic and rules of the application.

## [MVC Controllers](./controllers)

> Accepts input and converts it to commands for the model or view.

## [MVC Views](./views)

> Any representation of information such as a chart, diagram or table. Multiple views of the same information are possible, such as a bar chart for management and a tabular view for accountants.

## [Application factory](https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/)

> A common pattern is creating the application object when the blueprint is imported. But if you move the creation of this object into a function, you can then create multiple instances of this app later.

## [Database connections](./db.py)

## [Cache connections](./cache.py)

## [Custom exceptions](./exceptions.py)

## [Input Validations](./forms)
