import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
