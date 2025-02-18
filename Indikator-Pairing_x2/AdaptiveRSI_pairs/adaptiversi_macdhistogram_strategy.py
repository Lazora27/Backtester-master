import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'MACDHistogram': 1.0
        })
    )
