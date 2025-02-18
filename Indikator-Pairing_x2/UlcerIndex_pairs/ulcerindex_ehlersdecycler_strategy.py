import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
