import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
