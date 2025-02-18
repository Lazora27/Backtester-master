import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'WeightedCycle': 1.0
        })
    )
