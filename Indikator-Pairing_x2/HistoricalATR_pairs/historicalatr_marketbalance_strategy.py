import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und MarketBalance
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'MarketBalance': 1.0
        })
    )
