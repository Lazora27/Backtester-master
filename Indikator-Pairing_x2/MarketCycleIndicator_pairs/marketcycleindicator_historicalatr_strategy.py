import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'HistoricalATR': 1.0
        })
    )
