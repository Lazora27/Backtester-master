import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und CyberCycle
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'CyberCycle': 1.0
        })
    )
