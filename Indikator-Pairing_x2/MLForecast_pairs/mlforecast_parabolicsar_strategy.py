import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ParabolicSAR': 1.0
        })
    )
