import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'WeightedCycle': 1.0
        })
    )
