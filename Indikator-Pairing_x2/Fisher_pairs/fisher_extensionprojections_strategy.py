import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'ExtensionProjections': 1.0
        })
    )
