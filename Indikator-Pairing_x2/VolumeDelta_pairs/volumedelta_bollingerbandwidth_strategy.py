import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
