import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
