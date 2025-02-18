import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
