import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'MurreyMathLines': 1.0
        })
    )
