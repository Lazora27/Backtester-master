import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
