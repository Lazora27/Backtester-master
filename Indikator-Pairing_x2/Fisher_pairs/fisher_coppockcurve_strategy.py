import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'CoppockCurve': 1.0
        })
    )
