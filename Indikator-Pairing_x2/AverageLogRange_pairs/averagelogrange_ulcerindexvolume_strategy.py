import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
