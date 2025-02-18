import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
