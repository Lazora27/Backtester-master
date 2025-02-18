import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
