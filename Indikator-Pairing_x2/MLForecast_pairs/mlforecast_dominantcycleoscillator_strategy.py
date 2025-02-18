import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
