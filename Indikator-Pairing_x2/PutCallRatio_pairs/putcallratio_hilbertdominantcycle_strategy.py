import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
