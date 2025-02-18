import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und CyberCycle
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'CyberCycle': 1.0
        })
    )
