import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'MarketBalance': 1.0
        })
    )
