import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'StochasticRSI': 1.0
        })
    )
