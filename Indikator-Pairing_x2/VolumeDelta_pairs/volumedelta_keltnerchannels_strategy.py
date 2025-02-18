import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'KeltnerChannels': 1.0
        })
    )
