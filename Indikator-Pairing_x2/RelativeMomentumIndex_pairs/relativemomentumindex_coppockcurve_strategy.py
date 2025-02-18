import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'CoppockCurve': 1.0
        })
    )
