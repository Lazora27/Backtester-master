import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'EhlersDecycler': 1.0
        })
    )
