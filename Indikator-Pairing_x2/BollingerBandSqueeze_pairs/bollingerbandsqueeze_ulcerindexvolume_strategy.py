import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
