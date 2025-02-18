import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
