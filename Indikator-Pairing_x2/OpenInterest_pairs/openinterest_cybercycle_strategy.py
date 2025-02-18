import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und CyberCycle
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'CyberCycle': 1.0
        })
    )
