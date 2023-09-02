<script>
import {registerUser} from "@/services/UserService";

export default {
  name: "LoginView",
  data() {
    return {
      firstName: null,
      lastName: null,
      password: null,
      email: null
    }
  },
  methods: {
    registerClick() {
      let data = {
        email: this.email,
        password: this.password,
        first_name: this.firstName,
        last_name: this.lastName
      };
      registerUser(data)
          .then(response => {
            let responseData = response.data;
            console.log(responseData)
            this.$router.push("/auth/login")
          })
          .catch((error) => {
            alert(error.response.data.detail);
          });
    },
    emailInput(value) {
      this.email = value;
    },
    firstNameInput(value) {
      this.firstName = value;
    },
    lastNameInput(value) {
      this.lastName = value;
    },
    passwordInput(value) {
      this.password = value;
    }
  }
}

</script>

<template>
<div id="register">

<div id="formWrapper">
<div id="form">
<div class="logo">

</div>
    <h3 align="center">Registration</h3>
    <div class="form-item">
      <input type="email" :value="email" @input="emailInput($event.target.value)" placeholder="Email" id="email" class="form-style" autocomplete="off"/>
    </div>
     <div class="form-item">
      <input type="text" :value="firstName" @input="firstNameInput($event.target.value)" placeholder="First name" id="firstName" class="form-style" autocomplete="off"/>
    </div>
     <div class="form-item">
      <input type="text" :value="lastName" @input="lastNameInput($event.target.value)" placeholder="Last name" id="lastName" class="form-style" autocomplete="off"/>
    </div>
    <div class="form-item">
      <input type="password" placeholder="Password" :value="password" @input="passwordInput($event.target.value)" id="password" class="form-style" />
    </div>
    <div class="form-item">
        <router-link to="/auth/login" class="pull-left"><small>log in</small></router-link>
        <button class="btn login pull-right" @click="registerClick" style="background-color: #fff; border:1px solid #55b1df; color:#55b1df; cursor:pointer;">
          Register
        </button>
        <div class="clear-fix"></div>
    </div>
    <OAuth/>
</div>
</div>
</div>
</template>

<style>
@import '../assets/css/login.css';
</style>