import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'DPOCycles': 1.0
        })
    )
