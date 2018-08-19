import recastai

connect = recastai.Connect('023b08289cb13c6e96923628eccb4c45')

messages = [
  {
    'type': 'text',
    'content': 'Roger',
  }
]


connect.broadcast_message(messages)
