import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'SmoothedCycle': 1.0
        })
    )
