import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'EhlersDecycler': 1.0
        })
    )
