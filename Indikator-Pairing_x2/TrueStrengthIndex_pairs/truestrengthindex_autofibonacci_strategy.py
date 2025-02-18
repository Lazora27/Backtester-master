import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'AutoFibonacci': 1.0
        })
    )
