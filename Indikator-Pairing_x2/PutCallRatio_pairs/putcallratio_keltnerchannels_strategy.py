import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'KeltnerChannels': 1.0
        })
    )
