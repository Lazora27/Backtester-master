import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
