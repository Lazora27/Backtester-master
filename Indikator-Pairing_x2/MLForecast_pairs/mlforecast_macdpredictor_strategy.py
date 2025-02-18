import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'MACDPredictor': 1.0
        })
    )
