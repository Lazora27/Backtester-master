import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und BarStrength
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'BarStrength': 1.0
        })
    )
