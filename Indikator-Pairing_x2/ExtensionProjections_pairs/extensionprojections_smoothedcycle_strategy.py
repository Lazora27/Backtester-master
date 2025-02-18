import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'SmoothedCycle': 1.0
        })
    )
