import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
