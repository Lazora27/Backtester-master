import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
