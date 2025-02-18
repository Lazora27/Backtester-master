import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'ModifiedRSI': 1.0
        })
    )
