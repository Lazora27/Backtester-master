import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und CyberCycle
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'CyberCycle': 1.0
        })
    )
