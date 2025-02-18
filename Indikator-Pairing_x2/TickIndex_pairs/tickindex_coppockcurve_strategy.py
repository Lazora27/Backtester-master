import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'CoppockCurve': 1.0
        })
    )
