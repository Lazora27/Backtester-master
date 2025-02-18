import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und CyberCycle
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'CyberCycle': 1.0
        })
    )
