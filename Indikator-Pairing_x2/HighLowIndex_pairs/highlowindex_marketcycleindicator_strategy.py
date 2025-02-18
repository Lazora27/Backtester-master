import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
