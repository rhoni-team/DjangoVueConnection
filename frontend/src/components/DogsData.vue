<script setup>
import { ref, onMounted } from "vue";
import { getDogs } from "../api_connection/dogsRequest";

const dogs = ref([]);

onMounted(async () => {
   dogs.value = await getDogs();
});
</script>


<template>
   <div>
       <h1>Dogs</h1>
       <div v-for="dog in dogs" :key="dog.id">
           <div class="dog-data">
               <h2>{{ dog.name }}</h2>
               <ul>
                   <li>
                       Age: {{ dog.age }}
                   </li>
                   <li>
                       Color: {{ dog.color }}
                   </li>
                   <li>
                       Size: {{ dog.size }}
                   </li>
               </ul>
           </div>
       </div>
   </div>
</template>


<style scoped>
.dog-data {
   width: 250px;
   border: 1px solid #ccc;
   padding: 10px;
   margin: 10px;
   border-radius: 5px;
   box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
}
</style>
