import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
