import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'BuyingPressure': 1.0
        })
    )
