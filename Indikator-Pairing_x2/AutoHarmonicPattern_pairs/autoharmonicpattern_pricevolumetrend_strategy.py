import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
