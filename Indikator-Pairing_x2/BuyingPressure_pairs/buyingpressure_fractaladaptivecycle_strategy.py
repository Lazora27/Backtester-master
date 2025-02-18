import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_FractalAdaptiveCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und FractalAdaptiveCycle
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'FractalAdaptiveCycle': {
                'class': FractalAdaptiveCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalAdaptiveCycle'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'FractalAdaptiveCycle': 1.0
        })
    )
