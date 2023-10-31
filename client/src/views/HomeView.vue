<script setup lang="ts">
const { data } = useFetchCompanies()
</script>

<template>
  <main>
    <template v-if="data">
      <CompaniesBoard heading="자 이직할 시간이다 둘러봐라" :companies="data" />
    </template>
  </main>
</template>

<style></style>
