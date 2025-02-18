import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
