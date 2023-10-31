<script setup lang="ts">
defineProps<{
  heading: string
  companies: Company[]
}>()
</script>

<template>
  <section class="companies-board">
    <h2 class="companies-board__title">{{ heading }}</h2>
    <ul>
      <li>
        <CompanyCard
          v-for="company in companies"
          :company="company"
          :key="company.id"
        ></CompanyCard>
      </li>
    </ul>
  </section>
</template>

<style lang="scss" scoped>
.companies-board {
  margin: 12px 18px;
  padding: 18px 24px;
  &__title {
    margin: 18px;
    font-size: 1.6rem;
    font-weight: 600;
  }
}
</style>
