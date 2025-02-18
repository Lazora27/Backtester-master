import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'CycleFinder': 1.0
        })
    )
