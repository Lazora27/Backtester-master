import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
