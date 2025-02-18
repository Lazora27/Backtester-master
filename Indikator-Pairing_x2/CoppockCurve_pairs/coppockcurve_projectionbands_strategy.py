import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'ProjectionBands': 1.0
        })
    )
