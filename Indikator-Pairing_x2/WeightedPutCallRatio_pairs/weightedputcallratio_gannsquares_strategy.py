import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und GannSquares
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'GannSquares': 1.0
        })
    )
