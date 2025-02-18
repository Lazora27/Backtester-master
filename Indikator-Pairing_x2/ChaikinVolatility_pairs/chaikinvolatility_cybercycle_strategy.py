import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und CyberCycle
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'CyberCycle': 1.0
        })
    )
