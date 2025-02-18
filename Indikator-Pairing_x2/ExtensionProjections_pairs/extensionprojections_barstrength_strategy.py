import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und BarStrength
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'BarStrength': 1.0
        })
    )
