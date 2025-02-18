import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und CyberCycle
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'CyberCycle': 1.0
        })
    )
