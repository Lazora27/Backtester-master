import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'HullMovingAverage': 1.0
        })
    )
