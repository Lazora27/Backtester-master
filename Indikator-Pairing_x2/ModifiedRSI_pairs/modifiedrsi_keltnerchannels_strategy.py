import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'KeltnerChannels': 1.0
        })
    )
