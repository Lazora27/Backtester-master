import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
