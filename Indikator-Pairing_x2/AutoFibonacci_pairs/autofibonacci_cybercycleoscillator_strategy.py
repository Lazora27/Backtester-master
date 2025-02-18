import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
