import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und SuperTrend
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'SuperTrend': 1.0
        })
    )
