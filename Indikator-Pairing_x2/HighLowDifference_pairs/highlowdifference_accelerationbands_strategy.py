import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'AccelerationBands': 1.0
        })
    )
