import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
