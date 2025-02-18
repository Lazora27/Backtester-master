import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'EhlersDecycler': 1.0
        })
    )
