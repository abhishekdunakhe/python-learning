def https_error(number):

    match number:
        case 200:
            return "ok"
        case 404:
            return "page not found"
        case 500:
            return "Internal servre error"
        case _:
            return "Unknown error"


print(https_error(404))