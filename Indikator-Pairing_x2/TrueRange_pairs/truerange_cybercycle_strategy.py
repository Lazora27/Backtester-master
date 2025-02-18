import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und CyberCycle
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'CyberCycle': 1.0
        })
    )
