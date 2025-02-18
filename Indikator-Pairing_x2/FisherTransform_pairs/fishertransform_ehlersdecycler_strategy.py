import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'EhlersDecycler': 1.0
        })
    )
