const express = require("express");
// const bcrypt = require("bcrypt");

const router = express.Router();

const Users = require("../models/users");

router.post("/register", (req, res) => {

  let data = req.body;
  console.log(req.body);
  console.log(data);
  let user = new Users(data);
  
  /* salt = bcrypt.genSaltSync(10);
  user.password = bcrypt.hashSync(data.password, salt);
 */
  user
    .save()
    .then((savedUser) => {
      res.status(200).send(savedUser);
    })
    .catch((err) => {
      console.log(err);
    });
});

router.post("/login", (req, res) => {});

router.get("/all", (req, res) => {});

router.get("/getbyid/:id", (req, res) => {});

router.put("/update/:id", (req, res) => {});

module.exports = router;
