import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
