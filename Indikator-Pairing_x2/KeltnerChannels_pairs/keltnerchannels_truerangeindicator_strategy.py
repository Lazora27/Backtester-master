import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
