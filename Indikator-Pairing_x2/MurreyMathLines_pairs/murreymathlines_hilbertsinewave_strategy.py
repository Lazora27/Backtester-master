import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'HilbertSinewave': 1.0
        })
    )
