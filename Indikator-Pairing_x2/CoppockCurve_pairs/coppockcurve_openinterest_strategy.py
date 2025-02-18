import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und OpenInterest
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'OpenInterest': 1.0
        })
    )
