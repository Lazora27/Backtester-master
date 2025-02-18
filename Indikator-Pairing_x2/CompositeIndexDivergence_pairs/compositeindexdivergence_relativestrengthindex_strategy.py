import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
