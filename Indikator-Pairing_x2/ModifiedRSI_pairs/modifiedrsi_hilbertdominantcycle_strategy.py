import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
