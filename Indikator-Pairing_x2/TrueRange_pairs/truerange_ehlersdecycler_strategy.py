import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'EhlersDecycler': 1.0
        })
    )
