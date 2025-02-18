import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'KeltnerChannels': 1.0
        })
    )
