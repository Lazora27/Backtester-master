import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'DonchianChannels': 1.0
        })
    )
