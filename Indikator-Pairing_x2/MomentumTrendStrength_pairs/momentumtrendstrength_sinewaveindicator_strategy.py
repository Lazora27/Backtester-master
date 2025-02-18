import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
