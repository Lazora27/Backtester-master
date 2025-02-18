import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
