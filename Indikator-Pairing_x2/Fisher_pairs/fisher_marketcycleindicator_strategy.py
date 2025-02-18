import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
