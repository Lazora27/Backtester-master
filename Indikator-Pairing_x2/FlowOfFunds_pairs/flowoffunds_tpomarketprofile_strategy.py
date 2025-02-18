import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
