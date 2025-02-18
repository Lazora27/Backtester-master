import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
