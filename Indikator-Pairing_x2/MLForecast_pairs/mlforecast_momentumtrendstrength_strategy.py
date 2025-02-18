import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
