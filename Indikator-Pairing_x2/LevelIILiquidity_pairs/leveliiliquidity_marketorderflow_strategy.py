import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
