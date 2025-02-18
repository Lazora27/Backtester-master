import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
