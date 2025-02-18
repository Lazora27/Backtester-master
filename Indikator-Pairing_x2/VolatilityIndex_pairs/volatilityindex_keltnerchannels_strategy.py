import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
