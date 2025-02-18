import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
