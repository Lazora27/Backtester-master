import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und TimeCycle
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'TimeCycle': 1.0
        })
    )
