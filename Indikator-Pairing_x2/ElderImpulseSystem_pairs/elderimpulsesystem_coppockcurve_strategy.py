import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'CoppockCurve': 1.0
        })
    )
