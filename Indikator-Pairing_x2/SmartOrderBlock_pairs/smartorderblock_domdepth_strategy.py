import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und DOMDepth
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'DOMDepth': 1.0
        })
    )
