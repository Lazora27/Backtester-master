import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und PivotPoints
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'PivotPoints': 1.0
        })
    )
