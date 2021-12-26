from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.implicitly_wait(10)
    bot.change_currency(currency='USD')
    #bot.change_language(language="pt-pt")
    bot.select_place_to_go('Lisboa')
    bot.select_date(check_in_date='2021-12-28', check_out_date='2021-12-31')
    bot.select_passengers(adults = 1, rooms = 10)
    bot.search()
    bot.lowest_price_first()
    bot.apply_star_rating(rating=5)
    bot.refresh()
    bot.report_results()