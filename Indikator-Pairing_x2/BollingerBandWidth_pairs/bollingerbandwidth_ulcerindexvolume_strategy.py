import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
