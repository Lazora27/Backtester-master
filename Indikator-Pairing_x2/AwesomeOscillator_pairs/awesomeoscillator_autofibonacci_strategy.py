import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'AutoFibonacci': 1.0
        })
    )
