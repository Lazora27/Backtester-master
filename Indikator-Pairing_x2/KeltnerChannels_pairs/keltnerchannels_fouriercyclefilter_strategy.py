import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
