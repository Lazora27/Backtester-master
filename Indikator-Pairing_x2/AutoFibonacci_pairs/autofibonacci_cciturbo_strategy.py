import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und CCITurbo
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'CCITurbo': 1.0
        })
    )
