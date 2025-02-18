import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
