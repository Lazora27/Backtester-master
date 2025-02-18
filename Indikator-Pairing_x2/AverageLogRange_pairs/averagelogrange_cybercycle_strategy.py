import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und CyberCycle
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'CyberCycle': 1.0
        })
    )
