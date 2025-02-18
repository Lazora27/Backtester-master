import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ForecastOscillator': 1.0
        })
    )
