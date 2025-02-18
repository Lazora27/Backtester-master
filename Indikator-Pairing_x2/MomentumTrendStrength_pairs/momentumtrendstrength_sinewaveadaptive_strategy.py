import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
