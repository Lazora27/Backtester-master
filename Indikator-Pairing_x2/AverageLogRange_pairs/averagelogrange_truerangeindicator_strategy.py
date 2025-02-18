import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
