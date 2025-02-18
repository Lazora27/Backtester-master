import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'AverageLogRange': 1.0
        })
    )
