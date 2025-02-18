import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
