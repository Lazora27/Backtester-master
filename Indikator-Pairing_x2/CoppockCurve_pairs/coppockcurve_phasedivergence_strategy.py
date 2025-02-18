import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'PhaseDivergence': 1.0
        })
    )
