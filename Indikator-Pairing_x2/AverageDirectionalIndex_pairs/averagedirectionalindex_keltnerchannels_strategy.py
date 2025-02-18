import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
