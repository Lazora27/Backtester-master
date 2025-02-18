import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
