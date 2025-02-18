import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'HilbertTrendline': 1.0
        })
    )
