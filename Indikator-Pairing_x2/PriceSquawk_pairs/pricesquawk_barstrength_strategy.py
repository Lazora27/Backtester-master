import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und BarStrength
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'BarStrength': 1.0
        })
    )
