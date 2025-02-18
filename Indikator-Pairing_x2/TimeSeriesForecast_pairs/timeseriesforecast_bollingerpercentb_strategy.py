import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'BollingerPercentB': 1.0
        })
    )
