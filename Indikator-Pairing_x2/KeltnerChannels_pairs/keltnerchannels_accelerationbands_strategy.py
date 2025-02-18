import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'AccelerationBands': 1.0
        })
    )
