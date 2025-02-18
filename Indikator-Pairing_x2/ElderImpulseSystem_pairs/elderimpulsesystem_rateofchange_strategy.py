import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und RateOfChange
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'RateOfChange': 1.0
        })
    )
