import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
