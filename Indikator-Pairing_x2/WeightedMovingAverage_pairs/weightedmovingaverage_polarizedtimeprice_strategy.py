import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
