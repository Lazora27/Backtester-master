import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'EaseOfMovement': 1.0
        })
    )
