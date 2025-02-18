import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
