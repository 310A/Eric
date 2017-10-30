prefix = ' '
# text = '123drakeet'
text = '123 drakeet'

m = 'drakeet'
if (prefix + m) in text:
    text = text.replace(m, '@drakeet' + ' ')
else:
    text = text.replace(m, prefix + '@drakeet' + ' ')

print(text)
