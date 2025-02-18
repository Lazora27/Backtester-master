import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'DonchianChannels': 1.0
        })
    )
