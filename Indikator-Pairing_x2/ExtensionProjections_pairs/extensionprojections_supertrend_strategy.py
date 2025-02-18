import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und SuperTrend
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'SuperTrend': 1.0
        })
    )
