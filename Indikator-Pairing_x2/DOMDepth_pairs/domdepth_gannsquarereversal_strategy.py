import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'GannSquareReversal': 1.0
        })
    )
