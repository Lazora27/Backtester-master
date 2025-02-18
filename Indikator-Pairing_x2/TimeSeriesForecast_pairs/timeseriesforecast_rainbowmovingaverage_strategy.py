import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
