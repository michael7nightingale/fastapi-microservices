<script>
import {loginUser} from "@/services/UserService";
import {setUser} from "@/services/Auth";

export default {
  name: "LoginView",
  data(){
    return{
      email: null,
      password: null,
    }
  },
  methods: {
    loginClick(){
        let data;
        loginUser(this.email, this.password)
            .then((response) => {
              data = response.data;
              setUser(data.access_token)
              this.$router.push("/");
            })
            .catch((error) => {
              alert(error.response.data.detail);
            })
    },

    emailInput(value){
      this.email = value;
    },
    passwordInput(value){
      this.password = value;
    }
  }

}

</script>

<template>
<div id="form">
    <h3 align="center">Log in</h3>
    <div class="form-item">
      <label for="email">Email</label>
      <input type="text" placeholder="Email" :value="email" @input="emailInput($event.target.value)" id="email" class="form-style" autocomplete="off"/>
    </div>
    <div class="form-item">
      <label for="password">Password</label>
      <input type="password" placeholder="Password" :value="password" @input="passwordInput($event.target.value)" id="password" class="form-style" />
    </div>
    <div class="form-item row">
        <router-link :to="{name: 'register'}" class="pull-left"><small>register</small></router-link>
      <button class="btn login pull-right" @click="loginClick" style="background-color: #fff; border:1px solid #55b1df; color:#55b1df; cursor:pointer;">
        Log In
      </button>
        <div class="clear-fix"></div>
    </div>
</div>
</template>

<style>
@import '../assets/css/login.css';
</style>