import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'TrendCycles': 1.0
        })
    )
