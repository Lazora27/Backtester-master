import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
