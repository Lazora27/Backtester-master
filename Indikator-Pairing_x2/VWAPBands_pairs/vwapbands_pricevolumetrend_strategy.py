import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
