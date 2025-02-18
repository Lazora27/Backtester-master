import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
