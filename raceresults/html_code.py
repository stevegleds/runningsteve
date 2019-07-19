import pandas as pd


pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>

html_string = '''
<html>
  <head>
      <!-- Start Mui boilerplate code - used for mui css -->
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <!-- load MUI -->
      <link href="//cdn.muicss.com/mui-0.9.39/css/mui.min.css" rel="stylesheet" type="text/css" />
      <script src="//cdn.muicss.com/mui-0.9.39/js/mui.min.js"></script>
      <!-- End mui boilerplate code -->
  <title>Race Results</title></head>
  <link rel="stylesheet" type="text/css" href="df_style.css"/>
  </head>
  <body>
      <div class="mui-panel">Steve
        <button class="mui-btn mui-btn--raised"><a href="my_race_results.html">Sort by Date</a></a> </button>
        <button class="mui-btn mui-btn--raised"><a href="pace_my_race_results.html">Sort by Pace</a> </button>
        
    </div>
    <hr>
          <div class="mui-panel">Others
        <button class="mui-btn mui-btn--raised"><a href="summary_pace_others_race_results.html">Personal Best Times</a></a> </button>
        <button class="mui-btn mui-btn--raised"><a href="http://gledhill.xyz/sg/running/">Parkrun</a> </button>
        <button class="mui-btn mui-btn--raised"><a href="others_race_results.html">Sort by Date</a></a> </button>
        <button class="mui-btn mui-btn--raised"><a href="pace_others_race_results.html">Sort by Pace</a> </button>
        <button class="mui-btn mui-btn--raised"><a href="http://gledhill.xyz/sg/running/"></a> </button>
        <button class="mui-btn mui-btn--raised"><a href="baylee_pace_others_race_results.html">Baylee</a> </button>
        <button class="mui-btn mui-btn--raised"><a href="taylor_pace_others_race_results.html">Taylor</a> </button>
        <button class="mui-btn mui-btn--raised"><a href="aimee_pace_others_race_results.html">Aimee</a> </button>
    </div>
    <hr>
   <body>
    {table}
  </body>
</html>.
'''