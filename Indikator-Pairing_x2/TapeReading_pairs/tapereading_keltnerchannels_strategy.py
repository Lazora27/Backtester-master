import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'KeltnerChannels': 1.0
        })
    )
