import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'KeltnerChannels': 1.0
        })
    )
