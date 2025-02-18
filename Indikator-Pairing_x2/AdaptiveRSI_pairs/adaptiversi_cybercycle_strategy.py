import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und CyberCycle
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'CyberCycle': 1.0
        })
    )
