import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
