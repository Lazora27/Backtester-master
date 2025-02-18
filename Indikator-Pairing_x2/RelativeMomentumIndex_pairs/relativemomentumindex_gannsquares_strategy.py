import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und GannSquares
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'GannSquares': 1.0
        })
    )
