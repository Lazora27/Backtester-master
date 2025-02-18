import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und CyberCycle
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'CyberCycle': 1.0
        })
    )
