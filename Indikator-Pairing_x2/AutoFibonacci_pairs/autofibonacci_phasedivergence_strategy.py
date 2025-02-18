import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'PhaseDivergence': 1.0
        })
    )
