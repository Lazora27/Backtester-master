import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'EhlersDecycler': 1.0
        })
    )
