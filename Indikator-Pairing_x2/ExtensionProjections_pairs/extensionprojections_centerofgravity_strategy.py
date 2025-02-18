import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'CenterOfGravity': 1.0
        })
    )
