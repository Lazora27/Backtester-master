import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'CenterOfGravity': 1.0
        })
    )
