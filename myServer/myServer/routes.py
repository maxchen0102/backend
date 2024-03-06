def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('hello', '/hello')
    config.add_route('example_route', '/example_route')
    config.add_route('example_route2', '/example_route2')
    config.add_route('test_get', '/get')
    config.add_route('test_post', '/post')