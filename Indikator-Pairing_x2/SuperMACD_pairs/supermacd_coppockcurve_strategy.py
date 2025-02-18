import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'CoppockCurve': 1.0
        })
    )
