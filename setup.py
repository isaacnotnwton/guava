from distutils.core import setup, Extension

SRC_FOLDER = './src/'

guava_sources =[ SRC_FOLDER + name for name in [
    'guava_conn.c',
    'guava_handler/guava_handler.c',
    'guava_handler/guava_handler_static.c',
    'guava_mime_type.c',
    'guava_request.c',
    'guava_response.c',
    'guava_router/guava_router.c',
    'guava_router/guava_router_mvc.c',
    'guava_router/guava_router_rest.c',
    'guava_router/guava_router_static.c',
    'guava_server.c',
    'guava_string.c',
    'guava_session/guava_session.c',
    'guava_session/guava_session_store_inmem.c',
    'guava_session/guava_session_store_file.c',
    'guava_cookie.c'
]]

http_parser_include = ['deps/http-parser']
http_parser_files = ['deps/http-parser/http_parser.c']

compile_flags = ['-O0', '-ggdb', '-std=c99']

guava_module = Extension('guava',
                         sources=guava_sources + http_parser_files + [
                             SRC_FOLDER + 'guava_module/guava_module_request.c',
                             SRC_FOLDER + 'guava_module/guava_module_server.c',
                             SRC_FOLDER + 'guava_module/guava_module_handler.c',
                             SRC_FOLDER + 'guava_module/guava_module_controller.c',
                             SRC_FOLDER + 'guava_module/guava_module_router.c',
                             SRC_FOLDER + 'guava_module/guava_module_router_static.c',
                             SRC_FOLDER + 'guava_module/guava_module_router_mvc.c',
                             SRC_FOLDER + 'guava_module/guava_module_router_rest.c',
                             SRC_FOLDER + 'guava_module/guava_module_session.c',
                             SRC_FOLDER + 'guava_module/guava_module.c',
                             SRC_FOLDER + 'guava_module/guava_module_cookie.c',
                         ],
                         include_dirs=['./include/'] + http_parser_include,
                         library_dirs = [],
                         libraries=['uv'],
                         define_macros=[('HTTP_PARSER_STRICT', 1)],
                         extra_compile_args=compile_flags)

setup(name='guava',
      version='1.0',
      description='Guava - A super lightweight and high performance web framework for Python',
      author='Rock Lee',
      author_email='insfocus@gmail.com',
      maintainer='Rock Lee',
      maintainer_email='insfocus@gmail.com',
      ext_modules=[
          guava_module,
      ],
      license='BSD'
)
