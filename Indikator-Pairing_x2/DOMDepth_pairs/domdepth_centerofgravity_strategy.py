import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'CenterOfGravity': 1.0
        })
    )
