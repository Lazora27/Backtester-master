import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
