import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und CyberCycle
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'CyberCycle': 1.0
        })
    )
