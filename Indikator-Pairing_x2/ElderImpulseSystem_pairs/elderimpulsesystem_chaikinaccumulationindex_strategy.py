import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_ChaikinAccumulationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und ChaikinAccumulationIndex
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'ChaikinAccumulationIndex': {
                'class': ChaikinAccumulationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinAccumulationIndex'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'ChaikinAccumulationIndex': 1.0
        })
    )
