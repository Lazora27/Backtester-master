import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und MassIndex
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'MassIndex': 1.0
        })
    )
