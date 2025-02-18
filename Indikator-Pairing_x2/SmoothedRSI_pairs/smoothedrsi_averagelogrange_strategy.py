import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'AverageLogRange': 1.0
        })
    )
