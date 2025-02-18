import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'BuyingPressure': 1.0
        })
    )
