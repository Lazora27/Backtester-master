import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und OpenInterest
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'OpenInterest': 1.0
        })
    )
