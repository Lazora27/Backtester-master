import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'GannSquareReversal': 1.0
        })
    )
