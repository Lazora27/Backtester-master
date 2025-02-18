import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'FisherSignals': 1.0
        })
    )
