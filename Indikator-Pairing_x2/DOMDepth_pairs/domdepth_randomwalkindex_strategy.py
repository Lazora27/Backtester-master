import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
