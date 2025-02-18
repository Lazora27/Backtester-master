import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_CVIRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und CVIRatio
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'CVIRatio': 1.0
        })
    )
