import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und CycleFinder
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'CycleFinder': 1.0
        })
    )
