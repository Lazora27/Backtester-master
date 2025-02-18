import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und MarketBalance
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'MarketBalance': 1.0
        })
    )
