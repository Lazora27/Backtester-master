import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_MLForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und MLForecast
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'MLForecast': 1.0
        })
    )
