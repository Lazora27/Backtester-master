import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
