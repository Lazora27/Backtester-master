import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
