import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und FisherTransform
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'FisherTransform': 1.0
        })
    )
