import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'WeightedCycle': 1.0
        })
    )
