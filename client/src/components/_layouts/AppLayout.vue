<script setup lang="ts"></script>

<template>
  <AppHeader id="appHeader" />
  <main id="appMain">
    <slot></slot>
  </main>
</template>

<style lang="scss" scoped>
#appHeader {
  position: sticky;
  top: 0;
  max-width: 1060px;
  margin: 0 auto;
  padding: 12px 0;
}

#appMain {
  max-width: 1060px;
  margin: auto;
}
</style>
