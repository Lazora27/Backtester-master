import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und MarketBalance
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'MarketBalance': 1.0
        })
    )
