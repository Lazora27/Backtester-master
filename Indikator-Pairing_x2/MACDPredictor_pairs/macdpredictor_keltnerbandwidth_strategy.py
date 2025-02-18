import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
