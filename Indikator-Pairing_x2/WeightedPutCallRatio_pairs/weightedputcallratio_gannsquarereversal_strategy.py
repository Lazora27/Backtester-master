import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'GannSquareReversal': 1.0
        })
    )
