import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und BarStrength
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'BarStrength': 1.0
        })
    )
