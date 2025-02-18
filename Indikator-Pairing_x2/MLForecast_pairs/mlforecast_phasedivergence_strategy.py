import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'PhaseDivergence': 1.0
        })
    )
