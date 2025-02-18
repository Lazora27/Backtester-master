import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und DemandIndex
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'DemandIndex': 1.0
        })
    )
