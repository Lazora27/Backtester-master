import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'TRIXIndicator': 1.0
        })
    )
