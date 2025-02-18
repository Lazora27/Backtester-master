import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
