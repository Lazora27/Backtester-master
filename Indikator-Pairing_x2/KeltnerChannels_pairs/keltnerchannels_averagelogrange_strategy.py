import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'AverageLogRange': 1.0
        })
    )
