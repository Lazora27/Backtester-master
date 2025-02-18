import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
