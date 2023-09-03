<script>
import {getCategories} from "@/services/ShopService";

export default {
  name: "NavigationView",
  data(){
    return{
      categories: [],

    }
  },

  mounted(){
    getCategories()
        .then((response) => {
          this.categories = response.data;
        });
  }


}
</script>

<template>
<div class="container">
  <ul >
    <li clas="row" v-for="category in categories" :key="category">
      <router-link :to="{name: 'category', params: {category_id: `${category.id}`}}">{{ category.title }}</router-link>
    </li>
  </ul>
</div>
</template>

<style scoped>

</style>