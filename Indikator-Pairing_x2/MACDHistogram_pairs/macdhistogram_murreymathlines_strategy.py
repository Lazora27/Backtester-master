import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'MurreyMathLines': 1.0
        })
    )
