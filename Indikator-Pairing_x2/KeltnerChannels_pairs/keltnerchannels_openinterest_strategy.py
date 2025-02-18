import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und OpenInterest
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'OpenInterest': 1.0
        })
    )
