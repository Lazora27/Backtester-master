import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
