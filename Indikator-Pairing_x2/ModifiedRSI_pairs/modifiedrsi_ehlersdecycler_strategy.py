import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'EhlersDecycler': 1.0
        })
    )
