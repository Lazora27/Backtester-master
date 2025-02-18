import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'AverageLogRange': 1.0
        })
    )
