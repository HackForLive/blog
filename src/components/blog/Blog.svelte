<script>
  let htmlContent = ''
fetch('/build/petshop_cfg.html').then(response => {
  console.dir(response)
  return response.text();
}).then(html => {
  htmlContent = html
})
</script>

<main>
  <div class="content">{@html htmlContent}</div>
</main>

<style>
  main {
      text-align: center;
      padding: 1em;
      max-width: 240px;
      margin: 0 auto;
  }

  /* .content {
      text-align: center;
  } */
</style>
