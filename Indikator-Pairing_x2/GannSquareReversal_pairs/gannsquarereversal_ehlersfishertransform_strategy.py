import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
