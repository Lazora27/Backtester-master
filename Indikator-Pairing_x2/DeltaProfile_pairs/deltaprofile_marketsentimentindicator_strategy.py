import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
