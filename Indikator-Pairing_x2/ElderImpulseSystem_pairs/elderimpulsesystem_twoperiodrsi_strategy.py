import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
