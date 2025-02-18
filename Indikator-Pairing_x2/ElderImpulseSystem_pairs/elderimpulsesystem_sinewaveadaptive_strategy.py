import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
