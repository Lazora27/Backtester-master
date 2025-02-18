import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'CoppockCurve': 1.0
        })
    )
