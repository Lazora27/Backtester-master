import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'CoppockCurve': 1.0
        })
    )
