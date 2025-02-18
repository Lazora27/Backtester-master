import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'KeltnerChannels': 1.0
        })
    )
