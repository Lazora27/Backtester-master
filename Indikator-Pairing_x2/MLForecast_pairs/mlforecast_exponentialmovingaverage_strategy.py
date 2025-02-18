import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
