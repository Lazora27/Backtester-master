import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
