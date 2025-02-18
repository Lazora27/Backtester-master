import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
