import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
