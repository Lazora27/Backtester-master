import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'GannSquareReversal': 1.0
        })
    )
