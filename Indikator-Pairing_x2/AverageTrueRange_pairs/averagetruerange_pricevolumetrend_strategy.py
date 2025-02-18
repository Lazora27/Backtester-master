import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
