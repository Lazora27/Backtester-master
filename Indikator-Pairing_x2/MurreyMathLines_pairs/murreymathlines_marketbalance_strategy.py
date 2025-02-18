import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und MarketBalance
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'MarketBalance': 1.0
        })
    )
