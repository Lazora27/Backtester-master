import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
