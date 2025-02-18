import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und GannSquares
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'GannSquares': 1.0
        })
    )
