import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
