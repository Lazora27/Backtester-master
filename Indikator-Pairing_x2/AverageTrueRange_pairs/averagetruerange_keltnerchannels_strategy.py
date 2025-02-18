import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'KeltnerChannels': 1.0
        })
    )
