import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'WeightedCycle': 1.0
        })
    )
