import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
