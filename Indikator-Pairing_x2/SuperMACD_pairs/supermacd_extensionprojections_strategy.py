import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'ExtensionProjections': 1.0
        })
    )
