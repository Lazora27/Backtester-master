import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
