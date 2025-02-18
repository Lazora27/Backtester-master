import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
