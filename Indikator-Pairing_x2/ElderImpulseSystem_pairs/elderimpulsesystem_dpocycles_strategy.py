import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'DPOCycles': 1.0
        })
    )
