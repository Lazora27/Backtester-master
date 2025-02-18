import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und CycleFinder
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'CycleFinder': 1.0
        })
    )
