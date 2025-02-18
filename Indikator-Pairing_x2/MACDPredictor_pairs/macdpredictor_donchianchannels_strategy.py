import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'DonchianChannels': 1.0
        })
    )
