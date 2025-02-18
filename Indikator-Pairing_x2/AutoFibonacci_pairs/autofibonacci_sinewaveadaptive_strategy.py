import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
