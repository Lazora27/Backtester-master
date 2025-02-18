import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'ForecastOscillator': 1.0
        })
    )
