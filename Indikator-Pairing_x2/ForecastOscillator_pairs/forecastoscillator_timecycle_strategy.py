import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'TimeCycle': 1.0
        })
    )
