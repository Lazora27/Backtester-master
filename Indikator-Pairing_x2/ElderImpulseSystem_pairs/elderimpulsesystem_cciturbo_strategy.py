import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und CCITurbo
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'CCITurbo': 1.0
        })
    )
