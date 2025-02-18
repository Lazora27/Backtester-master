import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'CenterOfGravity': 1.0
        })
    )
