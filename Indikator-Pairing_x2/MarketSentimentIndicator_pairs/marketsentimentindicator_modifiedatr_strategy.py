import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'ModifiedATR': 1.0
        })
    )
