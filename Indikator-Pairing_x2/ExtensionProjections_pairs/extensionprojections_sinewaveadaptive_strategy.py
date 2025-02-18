import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
