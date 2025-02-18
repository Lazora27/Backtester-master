import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
