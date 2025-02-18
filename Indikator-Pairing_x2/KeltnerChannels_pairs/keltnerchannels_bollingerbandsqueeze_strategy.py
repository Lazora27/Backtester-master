import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
