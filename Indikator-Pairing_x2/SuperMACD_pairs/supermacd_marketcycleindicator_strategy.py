import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
