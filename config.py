BOT_API_TOKEN = '5664895970:AAFq5KhV4GpSaT0vo_XXNY-FFcjDN8nNqc8'
WEATHER_API_KEY = '8537d9ef6386cb97156fd47d832f479c'

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric')