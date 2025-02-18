import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und GannSquares
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'GannSquares': 1.0
        })
    )
