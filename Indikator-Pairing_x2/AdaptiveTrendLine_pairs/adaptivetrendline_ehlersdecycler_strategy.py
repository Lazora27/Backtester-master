import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'EhlersDecycler': 1.0
        })
    )
