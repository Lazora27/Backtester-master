import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
