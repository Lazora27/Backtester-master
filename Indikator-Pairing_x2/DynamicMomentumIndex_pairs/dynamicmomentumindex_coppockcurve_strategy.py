import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'CoppockCurve': 1.0
        })
    )
