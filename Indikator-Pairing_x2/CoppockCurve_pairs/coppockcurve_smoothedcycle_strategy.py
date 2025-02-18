import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'SmoothedCycle': 1.0
        })
    )
