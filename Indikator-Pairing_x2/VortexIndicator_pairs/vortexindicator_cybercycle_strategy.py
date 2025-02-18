import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und CyberCycle
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'CyberCycle': 1.0
        })
    )
