import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'CoppockCurve': 1.0
        })
    )
