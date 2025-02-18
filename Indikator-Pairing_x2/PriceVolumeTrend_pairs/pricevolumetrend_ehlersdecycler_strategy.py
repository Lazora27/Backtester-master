import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'EhlersDecycler': 1.0
        })
    )
