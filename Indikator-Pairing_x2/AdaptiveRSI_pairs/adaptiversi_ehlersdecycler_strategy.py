import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'EhlersDecycler': 1.0
        })
    )
