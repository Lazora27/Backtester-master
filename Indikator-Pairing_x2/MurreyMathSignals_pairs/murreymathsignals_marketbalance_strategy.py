import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und MarketBalance
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'MarketBalance': 1.0
        })
    )
