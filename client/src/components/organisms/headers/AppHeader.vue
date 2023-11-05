<script setup lang="ts"></script>

<template>
  <header class="app-header">
    <AppBrand class="app-header__brand" />
    <AppNavigation class="app-header__navigation" />
  </header>
</template>

<style lang="scss" scoped>
.app-header {
  display: flex;

  &__navigation {
    margin: 0 0 0 auto;
  }
}
</style>
