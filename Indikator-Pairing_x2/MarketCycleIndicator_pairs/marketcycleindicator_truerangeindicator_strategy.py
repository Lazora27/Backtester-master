import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
