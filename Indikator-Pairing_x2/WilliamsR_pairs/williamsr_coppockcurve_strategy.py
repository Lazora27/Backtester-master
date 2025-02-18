import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'CoppockCurve': 1.0
        })
    )
