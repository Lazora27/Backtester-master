import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
