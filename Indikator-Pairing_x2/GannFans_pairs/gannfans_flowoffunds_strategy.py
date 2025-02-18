import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'FlowOfFunds': 1.0
        })
    )
