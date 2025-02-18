import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'ExtensionProjections': 1.0
        })
    )
