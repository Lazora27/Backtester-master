import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
