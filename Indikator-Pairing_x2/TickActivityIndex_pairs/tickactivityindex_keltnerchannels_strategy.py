import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
