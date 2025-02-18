import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'WeightedCycle': 1.0
        })
    )
