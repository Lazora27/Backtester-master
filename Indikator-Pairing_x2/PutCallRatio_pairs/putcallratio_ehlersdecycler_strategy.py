import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'EhlersDecycler': 1.0
        })
    )
