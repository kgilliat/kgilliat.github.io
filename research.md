---
layout: page
title: Research
---
<style>
  .paper {
    padding: 1.4em 0;
    border-top: 1px solid #e5e5e5;
  }
  h2 + .paper {
    border-top: 0;
    padding-top: 0.25em;
  }
  .paper-title {
    font-weight: bold;
    line-height: 1.4;
  }
  .paper-meta {
    font-size: 0.92em;
    color: #555;
    margin-top: 0.3em;
    line-height: 1.5;
  }
  .paper-meta.presented {
    font-size: 0.8em;
    margin-top: 1.1em;
  }
  /* [ Abstract | Draft | Slides ] */
  .plinks {
    font-size: 0.9em;
    margin-top: 0.45em;
    color: #777;
  }
  .plinks a {
    color: #1a3a6c;
  }
  .plinks .sep {
    margin: 0 0.45em;
    color: #bbb;
  }
  .ptoggle {
    cursor: pointer;
  }
  .ptoggle:hover,
  .ptoggle:focus {
    text-decoration: underline;
  }
  /* Panels are visible without JavaScript; the inline script below hides
     them only once we know the toggles will work. */
  html.has-js .abstract-panel {
    display: none;
  }
  html.has-js .abstract-panel.open {
    display: block;
  }
  .abstract-panel {
    margin-top: 0.9em;
  }
  .paper-split {
    display: flex;
    gap: 1.6em;
    align-items: flex-start;
    margin-top: 0.9em;
  }
  .paper-split-text {
    flex: 1 1 auto;
    min-width: 0;
  }
  .paper-split-text > *:first-child {
    margin-top: 0;
  }
  .paper-split-text p,
  .abstract-panel p {
    margin-top: 0.75em;
    text-align: justify;
  }
  .abstract-label {
    font-weight: bold;
    color: #1a3a6c;
  }
  .paper-figure {
    margin: 0;
  }
  .paper-figure.side {
    flex: 0 0 36%;
  }
  .paper-figure img {
    width: 100%;
    height: auto;
    display: block;
    border: 1px solid #e5e5e5;
    border-radius: 3px;
  }
  .paper-figure figcaption {
    font-size: 0.75rem;
    color: #666;
    margin-top: 0.5em;
    line-height: 1.4;
  }
  @media only screen and (max-width: 700px) {
    .paper-split {
      flex-direction: column;
      gap: 1.2em;
    }
    .paper-figure.side {
      flex: 0 0 auto;
      max-width: 340px;
    }
  }
</style>
<script>document.documentElement.classList.add('has-js');</script>
## Job Market Paper

<div class="paper">
  <div class="paper-title"><a href="{{ '/papers/church_peers_on_politics_Gilliat_Brown.pdf' | relative_url }}">Partisan Effects of Religious Peer Groups</a></div>
  <div class="paper-meta">with <a href="https://jacobrbrown.com">Jacob Brown</a></div>
  <div class="plinks">[ <a href="{{ '/papers/church_peers_on_politics_Gilliat_Brown.pdf' | relative_url }}">Draft</a><span class="sep">|</span> <a href="{{ '/papers/JMP_slides.pdf' | relative_url }}">Slides</a> ]</div>
  <div class="paper-split">
    <div class="paper-split-text">
      <div class="abstract-label">Abstract</div>
      <p>How people shape each other's political affiliation is a central question in the social sciences&mdash;with broader implications for partisan sorting and polarization&mdash;but is difficult to answer because people select into peer groups. We study a natural experiment in which the Church of Jesus Christ of Latter-day Saints periodically redraws congregation assignment boundaries, reassigning members to new church peers. Linking records on every Utah registered voter from 2012&ndash;2021 to digitized congregation maps, we employ a spatial difference-in-discontinuities design that compares changes in party registration among voters who live near one another and start off in the same congregation but are assigned to different congregations. Voters conform to their new peers: Unaffiliated voters assigned to more Republican congregations become more likely to register Republican, and Republicans assigned to more Democratic congregations become more likely to leave the party. Reassigned boundaries show no relationship with prior registration changes, supporting the design&rsquo;s identifying assumption. The effects are not explained by correlated peer characteristics such as race or by the partisanship of congregation leaders. Effects are strongest between demographically similar peers, the members most likely to become friends, suggesting that influence operates through personal relationships among co-congregants.</p>
    </div>
    <figure class="paper-figure side">
      <a href="{{ '/images/figures/jmp_congregation_boundary_change.png' | relative_url }}">
        <img src="{{ '/images/figures/jmp_congregation_boundary_change.png' | relative_url }}" width="880" height="1485" alt="Two stacked maps of the same area. The 2014 map shows four colored congregation areas; the 2015 map overlays new boundaries in bold black, splitting the area into five.">
      </a>
      <figcaption>Example of a congregation boundary change: four congregations in 2014 become five in 2015, placing members who previously attended separate congregations together.</figcaption>
    </figure>
  </div>
  <div class="paper-meta presented">Presented at APSA, Boston (2026); ACLEC, UC Berkeley (2026); IRES Workshop, Chapman University (2026); ASREC Conference, Chapman University (2026); SOCAE Conference, UCLA (2025).</div>
</div>

## Working Papers

<div class="paper">
  <div class="paper-title"><a href="{{ '/papers/firm_closure_effects.pdf' | relative_url }}">The Effects of Firm Closures on Worker Outcomes: Evidence from Pre-War Utah</a></div>
  <div class="plinks">[ <a class="ptoggle" role="button" tabindex="0" data-target="abs-firm">Abstract</a><span class="sep">|</span> <a href="{{ '/papers/firm_closure_effects.pdf' | relative_url }}">Draft</a> ]</div>
  <div class="abstract-panel" id="abs-firm">
    <p>What was the role of firms in shaping workers&rsquo; careers historically and how much did it matter when their firm closed? To answer these questions, we construct an annual linked employer-employee panel for 1900&ndash;1940 from the city directories of Salt Lake City and Ogden, Utah, which listed every adult resident with his occupation, employer and address. Transcribing 76 editions and 3.6 million listings, we harmonize employers across editions, link men across editions and, through FamilySearch, to the complete-count censuses, and then validate the panel against the census. We show that firms played a major role in the pre-war urban economy. Most working-aged men were employed at a firm, and most career advancement occurred within firm. Using a stacked event study in which we compare men at failed firms to matched comparison men at surviving firms, we find that firm closure led to persistent negative effects on worker&rsquo;s labor market outcomes. Displaced men were 30 percentage points less likely to be listed with an employer a year later and 11 points less likely eight years later. One tenth moved away from the city and the rest were less likely to have steady employment and more likely to hold lower-status occupations. Marriage, fertility, and mortality were unaffected. Closures in 1930&ndash;1933, the early years of the Great Depression, were even more detrimental to worker outcomes.</p>
  </div>
</div>

## Selected Works in Progress

<div class="paper">
  <div class="paper-title">Out-Group Contact and Religious Switching</div>
  <div class="plinks">[ <a class="ptoggle" role="button" tabindex="0" data-target="abs-relsw">Abstract</a> ]</div>
  <div class="abstract-panel" id="abs-relsw">
    <p>How does out-group contact shape religious switching? The question is hard to study because shocks to contact are rare and religion is seldom measured at the granular level contact effects require. We study Latter-day Saint (LDS) Utah, where the religious divide was unusually salient, records of religious affiliation are unusually rich, and contact with other faiths can be observed as it grew from close to zero. The transcontinental railroad changed the territory&rsquo;s religious composition quickly with the non-LDS share of residents in Salt Lake City and Ogden rising from about 4 percent in 1870 to 14 percent by 1880. Because LDS church members migrated to Utah in pioneer companies, we identify initial religious affiliation from presence in a pioneer company roster and measure affiliation at the time of death by matching individuals to their obituaries which often list the church where a funeral was held. Among LDS pioneers who died as adults, 92 percent had an LDS funeral, 2 percent a funeral in another denomination, and 6 percent a funeral at a non religious location (e.g., funeral home). Religious switching increased across generations. Among pioneers&rsquo; grandchildren the shares were 89, 3 and 9 percent. Departure was more common among businessmen and higher earners, concentrated among those who stayed in the cities, and less common among former LDS missionaries and relatives of church leaders. Latter-day Saints in the four cities whose neighborhoods received more non-LDS residents were significantly more likely to have a funeral in another denomination, with a 10-percentage-point increase in a neighborhood&rsquo;s non-LDS share raising the probability by about 4 percentage points.</p>
  </div>
</div>

<div class="paper">
  <div class="paper-title">How Childhood Peer Groups Shape Long-Run Outcomes</div>
  <div class="plinks">[ <a class="ptoggle" role="button" tabindex="0" data-target="abs-peers">Abstract</a> ]</div>
  <div class="abstract-panel" id="abs-peers">
    <p>How do childhood peers shape upward mobility over the long run? This question is challenging to answer because families choose their neighborhoods and because neighborhoods bundle place-based treatments with peer effects. We study Utah from 1850 to 1940, where the Church of Jesus Christ of Latter-day Saints assigned families to congregations, called wards, according to geographic boundaries. Because historical ward boundaries rarely changed, we do not rely on boundary adjustments for identification. Instead, we define a child&rsquo;s peers as those ward-mates within two years of their age and compare siblings whose peers vary, which holds family characteristics and other place effects fixed. This is early-stage work, as we are still digitizing historic ward boundary maps. Preliminary results using Salt Lake City&rsquo;s original nineteen wards suggest that childhood ward peers mattered most in the marriage market. Adjusting for the number of potential partners available in each ward, individuals were more than twice as likely to marry someone from their own childhood ward as from a ward immediately across the street, and they married higher-status partners when better options were available in their ward. Effects on schooling and income are small and statistically insignificant.</p>
  </div>
</div>

<div class="paper">
  <div class="paper-title">Marriage Markets and Church Building: The Economics of Polygamy in the American West</div>
  <div class="plinks">[ <a class="ptoggle" role="button" tabindex="0" data-target="abs-marriage">Abstract</a> ]</div>
  <div class="abstract-panel" id="abs-marriage">
    <p>Who benefits and who loses when marriage norms change? Between 1852 and 1890, the Church of Jesus Christ of Latter-day Saints encouraged its members to practice polygamy while the federal government enacted increasingly strict laws to ban and prosecute it. This back-and-forth between church and state created a series of natural experiments which we exploit to study the impact of shifting the polygamy norm on both the marginal polygamists, and the marriage market as a whole. The largest shock was the Mormon Reformation of 1856&ndash;57, a religious revival movement that led to the doubling of the polygamy rate. By comparing marriageable-aged unmarried immigrant women who arrived during the Reformation to those who arrived just after, we find that a higher polygamy rate provided such women with better marriage options at no cost to their wellbeing. Specifically, they married sooner, to higher status and wealthier men, with no detectable harm to their longevity, fertility, or children. In contrast, we find that already-married women were harmed when their husband married an additional wife, with a shorter life expectancy of 1.2 years, consistent with a resource-sharing view of marriage. Finally, we show that polygamy did not crowd young men out of the marriage market. With high population growth and a tolerance for larger husband-wife age gaps, Utah sustained a moderate polygamy rate without creating a surplus of unmarried men.</p>
  </div>
</div>

<div class="paper">
  <div class="paper-title">Human Capital Beyond School: The Value Added of Non-School Institutions</div>
  <div class="paper-meta">with <a href="https://emileighharrison.github.io/index.html">Emileigh Harrison</a> and <a href="https://www.anthonyloktingyim.com/home">Anthony Yim</a></div>
  <div class="plinks">[ <a class="ptoggle" role="button" tabindex="0" data-target="abs-hc">Abstract</a> ]</div>
  <div class="abstract-panel" id="abs-hc">
    <p>Children build skills not only at home and in school, but also through organized social institutions outside school. Congregations, youth organizations, and other community institutions create repeated interactions with peers and adults, transmit information and norms, and provide mentoring and social support. Yet families select into these institutions, making their contribution to human-capital formation difficult to identify. We overcome this selection problem by exploiting a distinctive feature of the LDS Church: much like public schools assign students to geographically defined attendance zones, the Church assigns families to geographically defined congregations, called wards. Both ward and school boundaries are redrawn over time, creating changes in institutional assignment that do not require families to move. This project estimates social-institution value added, defined as the contribution of assignment to a non-school social institution to children&rsquo;s academic progress, and benchmarks its magnitude against traditional measures of school value added. We are currently in the process of applying for data access to Utah administrative K&ndash;12 records which will then be linked to time-varying ward and school boundaries. A cross-classified fixed-effects model would estimate ward and school contributions to standardized test-score growth, with identification and validation coming from nonmoving students whose ward or school assignment changes when boundaries are redrawn. We will then investigate mechanisms by examining whether social-institution value added is related to changes in peer composition, exposure to different adult role models and leaders, and the degree of overlap between students&rsquo; ward and school networks.</p>
  </div>
</div>

<div class="paper">
  <div class="paper-title">How Out-Group Contact Shapes Affect and Policy Preferences</div>
  <div class="paper-meta">with <a href="https://johnholbein.org">John Holbein</a> and <a href="https://myweb.fsu.edu/hanhassell4/">Hans Hassell</a></div>
  <div class="plinks">[ <a class="ptoggle" role="button" tabindex="0" data-target="abs-og">Abstract</a> ]</div>
  <div class="abstract-panel" id="abs-og">
    <p>Sustained contact with people unlike oneself is thought to shape affect toward out-groups and the formation of political preferences; however, empirical evidence is challenging to obtain because individuals usually choose who they interact with. The Church of Jesus Christ of Latter-day Saints assigns families to congregations by geographic boundary and periodically redraws those boundaries as local membership shifts, exogenously reassigning members to new peer groups. Our design compares members who belonged to the same congregation at baseline but were separated by a boundary change into congregations with different group compositions. Using a large-scale mail survey of Utah voters living near boundaries drawn since 2023, we plan to measure affect toward out-groups defined by race, party, and socioeconomic class, alongside views on a range of policies. Drawing on survey responses and linked voter records, we will construct peer-exposure measures that distinguish the effect of out-group contact from persuasion and information-sharing channels, and test how these channels shape change in affect and policy views over time. To trace dynamic effects, we will compare attitudes across boundaries drawn at different times, from within the last three months out to three years. The project is funded and currently in survey design.</p>
  </div>
</div>

## Other Publications

<div class="paper">
  <div class="paper-title"><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6792459/">Mortality Risk and Fine Particulate Air Pollution in a Large, Representative Cohort of U.S. Adults</a></div>
  <div class="paper-meta">with C. Arden Pope III, Jacob S. Lefler, Majid Ezzati, Joshua D. Higbee, Julian D. Marshall, Sun-Young Kim, Matthew Bechle, Spencer E. Vernon, Allen L. Robinson, and Richard T. Burnett</div>
  <div class="paper-meta"><em>Environmental Health Perspectives</em> (2019)</div>
  <div class="plinks">[ <a class="ptoggle" role="button" tabindex="0" data-target="abs-ehp">Abstract</a><span class="sep">|</span> <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6792459/">Published Version</a> ]</div>
  <div class="abstract-panel" id="abs-ehp">
    <p><strong>Background:</strong> Evidence indicates that air pollution contributes to cardiopulmonary mortality. There is ongoing debate regarding the size and shape of the pollution&ndash;mortality exposure&ndash;response relationship. There are also growing appeals for estimates of pollution&ndash;mortality relationships that use public data and are based on large, representative study cohorts.</p>
      <p><strong>Objectives:</strong> Our goal was to evaluate fine particulate matter air pollution (PM<sub>2.5</sub>) and mortality using a large cohort that is representative of the U.S. population and is based on public data. Additional objectives included exploring model sensitivity, evaluating relative effects across selected subgroups, and assessing the shape of the PM<sub>2.5</sub>&ndash;mortality relationship.</p>
      <p><strong>Methods:</strong> National Health Interview Surveys (1986&ndash;2014), with mortality linkage through 2015, were used to create a cohort of 1,599,329 U.S. adults and a subcohort with information on smoking and body mass index (BMI) of 635,539 adults. Data were linked with modeled ambient PM<sub>2.5</sub> at the census-tract level. Cox proportional hazards models were used to estimate PM<sub>2.5</sub>&ndash;mortality hazard ratios for all-cause and specific causes of death while controlling for individual risk factors and regional and urban versus rural differences.</p>
      <p><strong>Results:</strong> Estimated mortality hazard ratios, per 10 &micro;g/m<sup>3</sup> long-term exposure to PM<sub>2.5</sub>, were 1.12 (95% CI: 1.08, 1.15) for all-cause mortality, 1.23 (95% CI: 1.17, 1.29) for cardiopulmonary mortality, and 1.12 (95% CI: 1.00, 1.26) for lung cancer mortality. In general, PM<sub>2.5</sub>&ndash;mortality associations were consistently positive for all-cause and cardiopulmonary mortality across key modeling choices and across subgroups of sex, age, race-ethnicity, income, education levels, and geographic regions.</p>
      <p><strong>Discussion:</strong> This large, nationwide, representative cohort of U.S. adults provides robust evidence that long-term PM<sub>2.5</sub> exposure contributes to cardiopulmonary mortality risk. The ubiquitous and involuntary nature of exposures and the broadly observed effects across subpopulations underscore the public health importance of breathing clean air.</p>
  </div>
</div>

<script>
  document.querySelectorAll('.ptoggle').forEach(function (el) {
    function toggle(e) {
      e.preventDefault();
      var panel = document.getElementById(el.dataset.target);
      if (panel) panel.classList.toggle('open');
    }
    el.addEventListener('click', toggle);
    el.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') toggle(e);
    });
  });
</script>
