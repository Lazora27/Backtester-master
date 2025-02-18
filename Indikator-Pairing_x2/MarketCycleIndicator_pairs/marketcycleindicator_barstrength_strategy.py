import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und BarStrength
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'BarStrength': 1.0
        })
    )
