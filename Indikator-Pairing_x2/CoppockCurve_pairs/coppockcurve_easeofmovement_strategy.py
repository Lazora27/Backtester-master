import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'EaseOfMovement': 1.0
        })
    )
