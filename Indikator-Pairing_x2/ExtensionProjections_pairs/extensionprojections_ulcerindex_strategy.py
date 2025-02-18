import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'UlcerIndex': 1.0
        })
    )
