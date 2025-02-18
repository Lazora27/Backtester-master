import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
