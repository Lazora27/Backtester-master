import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und DOMDepth
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'DOMDepth': 1.0
        })
    )
