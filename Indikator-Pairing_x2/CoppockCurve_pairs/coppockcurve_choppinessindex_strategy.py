import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
