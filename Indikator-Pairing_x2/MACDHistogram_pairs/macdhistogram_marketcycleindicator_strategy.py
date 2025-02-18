import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
