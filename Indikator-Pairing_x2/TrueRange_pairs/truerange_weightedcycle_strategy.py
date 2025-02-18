import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'WeightedCycle': 1.0
        })
    )
