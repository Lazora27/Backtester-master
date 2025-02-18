import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und DemandIndex
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'DemandIndex': 1.0
        })
    )
