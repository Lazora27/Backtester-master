import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und GannAngles
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'GannAngles': 1.0
        })
    )
