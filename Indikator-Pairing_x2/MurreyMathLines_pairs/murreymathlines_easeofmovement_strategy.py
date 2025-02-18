import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'EaseOfMovement': 1.0
        })
    )
