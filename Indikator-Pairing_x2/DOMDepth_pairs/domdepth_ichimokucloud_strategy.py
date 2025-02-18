import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'IchimokuCloud': 1.0
        })
    )
