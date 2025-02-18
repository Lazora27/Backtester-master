import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceCycleOscillator_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceCycleOscillator und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'PriceCycleOscillator': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
