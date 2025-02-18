import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und VWAPBands
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'VWAPBands': 1.0
        })
    )
