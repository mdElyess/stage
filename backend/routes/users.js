const express = require("express");
const bcrypt = require("bcrypt");

const router = express.Router();
const jwt = require('jsonwebtoken')

const Users = require("../models/users");

router.post("/register", (req, res) => {

  let data = req.body;
  let user = new Users(data);
  
  salt = bcrypt.genSaltSync(10);
  user.password = bcrypt.hashSync(data.password, salt);
  user
    .save()
    .then((savedUser) => {
      res.status(200).send(savedUser);
    })
    .catch((err) => {
      console.log(err);
    });
    
});

router.post("/login", (req, res) => {
  let data = req.body;
  Users.findOne({email: data.email})
    .then(
      (user) => {
        let valid = bcrypt.compareSync(data.password, user.password)
        if (!valid) {
          res.send('password invalid')
        } else {
          let payload = {
            _id: user._id,
            email: user.email,
            fullname: user.name + ' ' + user.lastname
          }

          let token = jwt.sign(payload, '123456789')
          res.send({mytoken: token});
        }
      }
    ).catch(
      err => {
        res.send('email invalid')
        console.log(err);
      }
    )
});

router.get("/all", (req, res) => {});

router.get("/getbyid/:id", (req, res) => {});

router.put("/update/:id", (req, res) => {});

module.exports = router;
