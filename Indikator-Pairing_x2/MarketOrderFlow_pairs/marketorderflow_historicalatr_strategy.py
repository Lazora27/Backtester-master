import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'HistoricalATR': 1.0
        })
    )
