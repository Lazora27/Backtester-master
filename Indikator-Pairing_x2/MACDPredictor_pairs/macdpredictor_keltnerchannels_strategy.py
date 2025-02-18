import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'KeltnerChannels': 1.0
        })
    )
