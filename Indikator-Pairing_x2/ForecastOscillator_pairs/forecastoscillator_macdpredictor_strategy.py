import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'MACDPredictor': 1.0
        })
    )
