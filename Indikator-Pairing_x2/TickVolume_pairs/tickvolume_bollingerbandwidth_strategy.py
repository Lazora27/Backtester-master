import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
