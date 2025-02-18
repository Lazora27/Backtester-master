import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'EhlersDecycler': 1.0
        })
    )
