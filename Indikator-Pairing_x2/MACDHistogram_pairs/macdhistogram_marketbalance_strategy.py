import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und MarketBalance
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'MarketBalance': 1.0
        })
    )
