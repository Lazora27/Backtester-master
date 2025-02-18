import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
