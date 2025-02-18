import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'WeightedCycle': 1.0
        })
    )
