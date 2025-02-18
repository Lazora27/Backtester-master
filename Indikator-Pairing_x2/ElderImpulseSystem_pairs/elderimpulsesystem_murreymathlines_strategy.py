import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'MurreyMathLines': 1.0
        })
    )
