import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
