import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'EaseOfMovement': 1.0
        })
    )
