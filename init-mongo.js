db.createUser(
  {
    user: "preymongo",
    pwd: "preymongo123456",
    roles: [
      {
        role: "admin",
        db: "test"
      }
    ]
  }
)
