import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'CoppockCurve': 1.0
        })
    )
