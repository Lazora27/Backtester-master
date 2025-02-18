import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_FractalAdaptiveCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und FractalAdaptiveCycle
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'FractalAdaptiveCycle': {
                'class': FractalAdaptiveCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalAdaptiveCycle'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'FractalAdaptiveCycle': 1.0
        })
    )
