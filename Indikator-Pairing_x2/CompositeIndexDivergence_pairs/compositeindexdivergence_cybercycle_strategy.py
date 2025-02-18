import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und CyberCycle
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'CyberCycle': 1.0
        })
    )
