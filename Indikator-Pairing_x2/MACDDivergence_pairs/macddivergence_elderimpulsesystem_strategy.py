import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
