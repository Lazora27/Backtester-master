import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'FlowOfFunds': 1.0
        })
    )
