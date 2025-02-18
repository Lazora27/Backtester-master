import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und VWAPBands
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'VWAPBands': 1.0
        })
    )
