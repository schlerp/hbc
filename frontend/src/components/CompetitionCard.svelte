<script lang="ts">
  import { push } from "svelte-spa-router";
  import type { ICompetition } from "../types";

  console.log("CompetitionCard loaded...");

  export let competition: ICompetition;

  function formatDate(date: Date) {
    let tempDate = new Date(date);
    return tempDate.toDateString();
  }

  function handleClick(competitionId: string) {
    push(`/comps/${competitionId}`);
  }
</script>

<div class="row">
  <div
    class="card"
    on:click={() => {
      handleClick(`${competition.competitionId}`);
    }}
  >
    <div class="cardRow">
      <p class="desc item">{competition.description}</p>
      <ul class="allowedStyles item">
        {#each competition.allowedStyles as style}
          <li>{style.category}{style.subcategory} - {style.name}</li>
        {/each}
      </ul>
    </div>
    <div class="cardRow">
      <!-- <p class="name item">{competition.competitionId}</p> -->
      <p class="entryDate item">
        {formatDate(competition.entriesCloseDate)}
      </p>
      <p class="awardDate item">{formatDate(competition.awardsDate)}</p>
    </div>
  </div>
</div>

<style>
  ul {
    list-style: none;
  }
  .desc,
  .allowedStyles,
  .entryDate,
  .awardDate {
    width: 200px;
    padding: 0px;
  }
  .row {
    margin: calc(var(--spacing) * 2);
  }
  .cardRow {
    display: flex;
    flex-direction: row;
  }
  .card {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    justify-content: center;
    justify-items: center;
    border-radius: var(--spacing);
    box-shadow: 2px 2px 3px 0px var(--pal-text-soft),
      3px 3px 5px 0px var(--pal-text-soft);
    cursor: pointer;
    background-color: #ffffff;
  }
  .item {
    justify-self: center;
    margin: calc(var(--spacing) * 2);
  }
  .entryDate::before {
    content: "Entries Close";
    display: flex;
    top: -1rem;
    color: var(--pal-text-soft);
    font-size: 0.8rem;
  }
  .awardDate::before {
    content: "Awards Date";
    display: flex;
    top: -1rem;
    color: var(--pal-text-soft);
    font-size: 0.8rem;
  }
  .desc::before {
    content: "Competition Details";
    display: flex;
    top: -1rem;
    color: var(--pal-text-soft);
    font-size: 0.8rem;
  }
  .allowedStyles::before {
    content: "Allowed Styles";
    display: flex;
    top: -1rem;
    color: var(--pal-text-soft);
    font-size: 0.8rem;
  }
</style>
