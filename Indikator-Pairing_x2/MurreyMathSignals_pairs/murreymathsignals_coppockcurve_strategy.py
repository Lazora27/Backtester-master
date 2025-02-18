import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'CoppockCurve': 1.0
        })
    )
