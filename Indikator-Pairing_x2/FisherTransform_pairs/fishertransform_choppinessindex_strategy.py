import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
