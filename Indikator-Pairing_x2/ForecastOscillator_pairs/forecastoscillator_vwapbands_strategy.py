import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und VWAPBands
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'VWAPBands': 1.0
        })
    )
