import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
