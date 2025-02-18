import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'ModifiedATR': 1.0
        })
    )
