import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und TrueRange
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'TrueRange': 1.0
        })
    )
