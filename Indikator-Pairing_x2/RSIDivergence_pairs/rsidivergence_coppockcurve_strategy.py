import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'CoppockCurve': 1.0
        })
    )
