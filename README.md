# Folder Structure

src: contains all our code

  /layer -> contains the code which will go into lambda layers
    /api_helpers -> contains the business logic
    /aws_helpers -> contains helper functions to interact with aws service like db helpers
    /logger
    /util
  /entities

Note: swagger.yaml cannot be empty

commands:
- sam build
- sam deploy
