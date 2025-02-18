import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
