import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und GannSquares
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'GannSquares': 1.0
        })
    )
