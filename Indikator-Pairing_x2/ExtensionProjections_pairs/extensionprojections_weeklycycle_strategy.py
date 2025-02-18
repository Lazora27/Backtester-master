import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'WeeklyCycle': 1.0
        })
    )
