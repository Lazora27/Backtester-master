import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
