import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'FlowOfFunds': 1.0
        })
    )
