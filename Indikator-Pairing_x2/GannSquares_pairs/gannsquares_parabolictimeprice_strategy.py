import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
