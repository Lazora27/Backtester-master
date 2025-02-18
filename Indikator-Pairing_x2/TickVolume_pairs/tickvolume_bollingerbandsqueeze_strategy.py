import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
