import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und CyberCycle
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'CyberCycle': 1.0
        })
    )
