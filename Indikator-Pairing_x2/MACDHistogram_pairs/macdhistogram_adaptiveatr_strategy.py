import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'AdaptiveATR': 1.0
        })
    )
