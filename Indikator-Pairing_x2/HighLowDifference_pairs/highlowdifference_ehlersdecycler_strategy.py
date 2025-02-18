import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'EhlersDecycler': 1.0
        })
    )
