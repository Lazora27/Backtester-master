import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'MomentumIndicator': 1.0
        })
    )
