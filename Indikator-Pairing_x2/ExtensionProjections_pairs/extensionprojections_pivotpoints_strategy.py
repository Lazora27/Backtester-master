import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und PivotPoints
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'PivotPoints': 1.0
        })
    )
