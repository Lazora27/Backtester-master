import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
