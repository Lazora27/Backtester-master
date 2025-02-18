import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
