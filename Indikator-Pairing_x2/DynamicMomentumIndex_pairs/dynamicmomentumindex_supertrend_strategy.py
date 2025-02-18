import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und SuperTrend
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'SuperTrend': 1.0
        })
    )
