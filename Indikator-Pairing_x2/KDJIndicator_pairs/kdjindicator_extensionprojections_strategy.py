import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'ExtensionProjections': 1.0
        })
    )
