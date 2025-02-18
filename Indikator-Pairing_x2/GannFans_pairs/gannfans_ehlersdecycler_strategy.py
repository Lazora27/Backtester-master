import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'EhlersDecycler': 1.0
        })
    )
