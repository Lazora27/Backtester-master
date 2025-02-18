import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
