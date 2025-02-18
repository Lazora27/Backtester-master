import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und BarStrength
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'BarStrength': 1.0
        })
    )
