import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
