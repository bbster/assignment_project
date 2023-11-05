<script setup lang="ts">
defineProps<{
  heading: string
  companies: Company[]
}>()
</script>

<template>
  <section class="companies-board">
    <h2 class="companies-board__title">{{ heading }}</h2>
    <div class="companies-board__contents">
      <ul class="companies-board__contents__cards">
        <li
          class="companies-board__contents__cards__item"
          v-for="company in companies"
          :key="company.id"
        >
          <CompanyCard class="companies-board__contents__cards__item__card" :company="company" />
        </li>
      </ul>
    </div>
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
    word-break: keep-all;
  }
  &__contents {
    &__cards {
      display: flex;
      flex-wrap: wrap;
      &__item {
        width: 25%;
        @media (min-width: 768px) and (max-width: 991px) {
          width: 50%;
        }
        @media (max-width: 768px) {
          width: 100%;
        }
        &__card {
          min-height: 140px;
          width: auto;
        }
      }
    }
  }
}
</style>
