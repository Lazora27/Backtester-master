import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
