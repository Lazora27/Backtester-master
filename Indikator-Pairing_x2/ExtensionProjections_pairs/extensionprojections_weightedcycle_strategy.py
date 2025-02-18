import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'WeightedCycle': 1.0
        })
    )
