import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
