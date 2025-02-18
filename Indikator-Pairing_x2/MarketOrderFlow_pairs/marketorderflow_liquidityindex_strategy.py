import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'LiquidityIndex': 1.0
        })
    )
