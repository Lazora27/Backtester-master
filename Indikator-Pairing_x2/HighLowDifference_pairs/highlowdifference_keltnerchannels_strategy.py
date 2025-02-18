import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'KeltnerChannels': 1.0
        })
    )
