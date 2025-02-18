import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'CCITurbo': 1.0
        })
    )
