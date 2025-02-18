import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'TickActivityIndex': 1.0
        })
    )
