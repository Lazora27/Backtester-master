import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
