import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SineWaveOscillator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SineWaveOscillator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'SineWaveOscillator': 1.0,
            'TrendCycles': 1.0
        })
    )
