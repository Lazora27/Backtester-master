import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und RateOfChange
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'RateOfChange': 1.0
        })
    )
