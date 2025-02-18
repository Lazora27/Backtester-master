import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
