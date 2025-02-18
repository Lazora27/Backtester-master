import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
