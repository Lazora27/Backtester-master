import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'KeltnerChannels': 1.0
        })
    )
