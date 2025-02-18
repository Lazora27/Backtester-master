import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und TrendCycles
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'TrendCycles': 1.0
        })
    )
