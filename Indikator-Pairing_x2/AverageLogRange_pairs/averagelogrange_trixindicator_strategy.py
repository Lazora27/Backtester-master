import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'TRIXIndicator': 1.0
        })
    )
