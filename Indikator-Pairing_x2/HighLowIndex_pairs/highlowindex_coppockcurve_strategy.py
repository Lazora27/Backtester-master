import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'CoppockCurve': 1.0
        })
    )
