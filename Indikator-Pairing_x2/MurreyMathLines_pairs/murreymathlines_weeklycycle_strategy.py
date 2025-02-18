import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'WeeklyCycle': 1.0
        })
    )
