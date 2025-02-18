import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
