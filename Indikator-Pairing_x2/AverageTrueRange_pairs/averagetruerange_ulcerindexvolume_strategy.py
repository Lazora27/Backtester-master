import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
