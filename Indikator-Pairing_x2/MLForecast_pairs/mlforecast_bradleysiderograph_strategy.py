import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'BradleySiderograph': 1.0
        })
    )
