import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
