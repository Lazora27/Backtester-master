import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und FisherTransform
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'FisherTransform': 1.0
        })
    )
