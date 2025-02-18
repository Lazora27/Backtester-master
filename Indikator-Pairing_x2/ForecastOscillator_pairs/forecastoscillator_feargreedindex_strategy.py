import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'FearGreedIndex': 1.0
        })
    )
