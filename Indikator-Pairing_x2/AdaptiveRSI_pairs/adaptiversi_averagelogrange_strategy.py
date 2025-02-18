import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'AverageLogRange': 1.0
        })
    )
