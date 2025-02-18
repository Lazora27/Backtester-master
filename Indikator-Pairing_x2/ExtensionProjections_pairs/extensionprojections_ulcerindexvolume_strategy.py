import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
