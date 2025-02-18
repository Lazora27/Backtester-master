import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'EhlersDecycler': 1.0
        })
    )
