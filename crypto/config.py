params = {
  # crypto setup
  'currency_1': 'BTC', # Bitcoin
  'currency_2': 'ETH', # Ethereum
  'currency_3': 'LINK', # Chainlink
  'ref_currency': 'USD',
  'ma': 25,
  # api setup
  'api_call_period': 5,
}

config = {
  # kafka
  'kafka_broker': 'localhost:9092',
  # topics
  'topic_1': f"topic_{params['currency_1']}",
  'topic_2': f"topic_{params['currency_2']}",
  'topic_3': f"topic_{params['currency_3']}",
  'topic_4': f"topic_{params['currency_1']}_ma_{params['ma']}",
  'topic_5': f"topic_{params['currency_2']}_ma_{params['ma']}",
  'topic_6': f"topic_{params['currency_3']}_ma_{params['ma']}",
}