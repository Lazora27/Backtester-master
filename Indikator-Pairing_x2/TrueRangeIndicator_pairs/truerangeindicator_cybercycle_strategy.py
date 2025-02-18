import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und CyberCycle
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'CyberCycle': 1.0
        })
    )
