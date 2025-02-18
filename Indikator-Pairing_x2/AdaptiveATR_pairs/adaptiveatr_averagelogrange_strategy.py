import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'AverageLogRange': 1.0
        })
    )
