Weather-python
---
### Basic usage:

Weather-python is Japanese forecast script tool.　Weather information is using the "livedoor 天気情報".

1. Find the available city. You select state from
47 prefectures.
```
$ python weather.py cities -s '東京都'
東京,大島,八丈島,父島
```

2. Show the tomorrow forecast of the city.
```
$ python weather.py forecasts -tt -c '東京'
2016-02-21 forecasts:晴時々曇 max celsius:16 min celsius:9
```

### Install
Required python 2.7.5 over, maybe.
```
$ git clone git@github.com:arvelt/weather-python.git
cd weather-python
python weather.py
```


### Usage detail:

Weather-python has subcommands.

__cities__  
Find available cities from states name. You input state like this "\*\*県"  
```
Usage: weather.py cities [OPTIONS]

Options:
  -s, --state TEXT  Show cities list from state.
  --help            Show this message and exit.
```

__forecasts__  
Show the weather information of the city. Without `-c` options, show the forecasts of 東京. Without `-t` `-tt` `-ttt` options, show the today forecasts.
```
Usage: weather.py forecasts [OPTIONS]

Options:
  -t, --today            Show the today weather.
  -tt, --tomorrow        Show the tomorrow weather.
  -ttt, --aftertomorrow  Show the day after tomorrow weather.
  -c, --city TEXT        The city name to see the weather.
  --help                 Show this message and exit.
```

### TODO
- Rename state to prefectures.
- cities -s validation
- Add subcommand to show prefectures list.
- Use pip to install.
- Adjusting directory.
- Code refactoring.
- More like CLI.
- Add test.
- Deploy CI.
