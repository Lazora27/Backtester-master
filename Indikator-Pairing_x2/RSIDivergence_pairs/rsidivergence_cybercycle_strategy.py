import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und CyberCycle
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'CyberCycle': 1.0
        })
    )
