import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeTrendIndicator_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeTrendIndicator und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'VolumeTrendIndicator': 1.0,
            'EhlersDecycler': 1.0
        })
    )
