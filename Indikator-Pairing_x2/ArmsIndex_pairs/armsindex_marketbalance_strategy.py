import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
