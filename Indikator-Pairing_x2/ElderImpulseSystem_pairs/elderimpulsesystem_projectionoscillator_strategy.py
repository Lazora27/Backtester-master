import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
