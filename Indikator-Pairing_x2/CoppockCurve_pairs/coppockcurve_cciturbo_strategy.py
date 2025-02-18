import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und CCITurbo
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'CCITurbo': 1.0
        })
    )
