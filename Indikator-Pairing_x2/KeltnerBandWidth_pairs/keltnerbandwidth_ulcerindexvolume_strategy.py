import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
