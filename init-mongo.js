db.createUser(
  {
    user: "mongo",
    pwd: "111111",
    roles: [
      {
        role: "readWrite",
        db: "test"
      }
    ]
  }
)
