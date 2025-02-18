import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
