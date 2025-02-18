import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
