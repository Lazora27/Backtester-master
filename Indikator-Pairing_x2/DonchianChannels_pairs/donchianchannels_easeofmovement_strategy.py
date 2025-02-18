import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'EaseOfMovement': 1.0
        })
    )
