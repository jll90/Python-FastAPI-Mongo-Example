db.createUser(
  {
    user: "preymongo",
    pwd: "preymongo123456",
    roles: [
      {
        role: "readWrite",
        db: "local"
      }
    ]
  }
)
