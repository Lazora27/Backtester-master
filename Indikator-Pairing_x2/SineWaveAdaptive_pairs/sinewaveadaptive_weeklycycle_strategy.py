import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SineWaveAdaptive_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SineWaveAdaptive und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'SineWaveAdaptive': 1.0,
            'WeeklyCycle': 1.0
        })
    )
