<script setup lang="ts">
const { data } = useFetchCompanies()
</script>

<template>
  <AppLayout>
    <template v-if="data">
      <CompaniesBoard heading="자 이직할 시간이다 둘러봐라" :companies="data" />
    </template>
  </AppLayout>
</template>

<style></style>
