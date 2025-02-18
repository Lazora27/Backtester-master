import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und CyberCycle
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'CyberCycle': 1.0
        })
    )
