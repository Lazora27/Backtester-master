import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und SuperTrend
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'SuperTrend': 1.0
        })
    )
