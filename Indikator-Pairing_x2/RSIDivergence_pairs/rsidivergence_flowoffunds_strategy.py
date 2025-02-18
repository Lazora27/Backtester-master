import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'FlowOfFunds': 1.0
        })
    )
