import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'FlowOfFunds': 1.0
        })
    )
