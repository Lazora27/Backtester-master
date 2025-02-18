import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und DOMDepth
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'DOMDepth': 1.0
        })
    )
