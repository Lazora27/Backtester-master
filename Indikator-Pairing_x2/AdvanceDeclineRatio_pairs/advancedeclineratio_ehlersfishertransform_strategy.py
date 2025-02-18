import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineRatio_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineRatio und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineRatio': {
                'class': AdvanceDeclineRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineRatio'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'AdvanceDeclineRatio': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
