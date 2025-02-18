import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_NormalizedAverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und NormalizedAverageTrueRange
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'NormalizedAverageTrueRange': {
                'class': NormalizedAverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedAverageTrueRange'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'NormalizedAverageTrueRange': 1.0
        })
    )
