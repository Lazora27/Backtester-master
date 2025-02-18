import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
