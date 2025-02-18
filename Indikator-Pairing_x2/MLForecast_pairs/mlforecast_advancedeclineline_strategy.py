import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_AdvanceDeclineLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und AdvanceDeclineLine
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'AdvanceDeclineLine': 1.0
        })
    )
