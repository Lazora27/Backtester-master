import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'WeeklyCycle': 1.0
        })
    )
