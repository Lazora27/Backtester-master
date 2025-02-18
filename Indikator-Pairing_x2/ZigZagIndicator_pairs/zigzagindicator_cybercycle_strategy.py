import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und CyberCycle
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'CyberCycle': 1.0
        })
    )
