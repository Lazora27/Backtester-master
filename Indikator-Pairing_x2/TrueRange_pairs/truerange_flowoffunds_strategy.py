import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'FlowOfFunds': 1.0
        })
    )
