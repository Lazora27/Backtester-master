import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
