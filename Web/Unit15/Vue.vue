<template>
  <div>
    <h1>Data</h1>
    <ul>
      <li v-for="item in data" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      data: []
    }
  },
  mounted() {
    axios.get('https://api.example.com/data')
      .then(response => this.data = response.data);
  }
}
</script>