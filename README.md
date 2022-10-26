# Daily Currency Conversion Email

```diff
 Objective: Email daily about the currency conversion rate of Dollar($) and Euro(€) to Nepali Ruppees(NPR)
```

I scraped the forex data from https://www.laxmibank.com/rates/forex/ and arranged it in a dataframe and scheduled it to email every 11:45 
AM NPT except on the weekends since the forex data will not be updated on the weekends.


<img width='50%' src='https://raw.github.com/thesumitshrestha/daily-currency-email/main/currency-output.png' />
