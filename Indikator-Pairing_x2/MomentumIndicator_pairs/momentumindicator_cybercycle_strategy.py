import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und CyberCycle
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'CyberCycle': 1.0
        })
    )
