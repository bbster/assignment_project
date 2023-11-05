<script setup lang="ts">
const props = defineProps<{ company: Company }>()

const addr = computed(() => `${props.company.country} . ${props.company.city}`)
</script>

<template>
  <article class="company-card">
    <h2 class="company-card__title">{{ company.company_name }}</h2>
    <div>
      <p class="company-card__addr">{{ addr }}</p>
    </div>
  </article>
</template>

<style lang="scss" scoped>
.company-card {
  margin: 8px;
  padding: 18px 24px;
  box-shadow: 2px 2px 4px #dddddd;
  border-radius: 4%;
  &__title {
    min-height: 2.4em;
    margin: 12px 0;
    font-size: 1em;
    font-weight: 600;
    word-break: keep-all;
  }
  &__addr {
    margin: 8px 0;
    font-size: 0.8em;
    text-align: right;
  }
}
</style>
