import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
