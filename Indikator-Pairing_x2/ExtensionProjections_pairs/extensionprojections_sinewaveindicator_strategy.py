import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
