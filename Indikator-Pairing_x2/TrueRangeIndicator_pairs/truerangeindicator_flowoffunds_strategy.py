import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'FlowOfFunds': 1.0
        })
    )
