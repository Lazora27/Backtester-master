import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
