import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
