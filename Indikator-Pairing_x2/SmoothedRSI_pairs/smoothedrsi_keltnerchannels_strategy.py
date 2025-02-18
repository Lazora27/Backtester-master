import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'KeltnerChannels': 1.0
        })
    )
