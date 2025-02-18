import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
