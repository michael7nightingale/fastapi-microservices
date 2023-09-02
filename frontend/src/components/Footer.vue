<script>
export default {
  name: 'FooterComponent',
  computed: {
    Year() {
      return new Date().getFullYear().toString();
    },
  },

}
</script>

<template>
  <div class="footer-bottom-area">
        <div class="container">
            <div class="row">
                <div class="col-md-8">
                    <div class="copyright">
                        <p>&copy; {{ Year }} All Rights Reserved.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>
@import "../assets/css/style.css";
</style>
