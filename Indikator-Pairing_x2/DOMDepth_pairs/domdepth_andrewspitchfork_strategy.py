import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
