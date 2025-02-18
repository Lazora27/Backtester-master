import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'FlowOfFunds': 1.0
        })
    )
