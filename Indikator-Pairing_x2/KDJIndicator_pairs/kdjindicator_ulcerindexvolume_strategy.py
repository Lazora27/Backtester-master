import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
