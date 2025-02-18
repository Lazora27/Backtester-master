import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'BuyingPressure': 1.0
        })
    )
