import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'WeightedCycle': 1.0
        })
    )
