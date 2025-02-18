import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'EhlersDecycler': 1.0
        })
    )
