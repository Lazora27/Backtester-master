import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
