import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
