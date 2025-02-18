import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und DOMDepth
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'DOMDepth': 1.0
        })
    )
