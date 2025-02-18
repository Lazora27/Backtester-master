import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'LiquidityIndex': 1.0
        })
    )
