import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und OpenInterest
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'OpenInterest': 1.0
        })
    )
