import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und GannAngles
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'GannAngles': 1.0
        })
    )
