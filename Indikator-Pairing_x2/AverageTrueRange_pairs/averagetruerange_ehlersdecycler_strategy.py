import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'EhlersDecycler': 1.0
        })
    )
