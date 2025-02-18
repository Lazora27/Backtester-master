import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiSmoothed_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiSmoothed und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'HeikenAshiSmoothed': {
                'class': HeikenAshiSmoothed,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiSmoothed'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'HeikenAshiSmoothed': 1.0,
            'KeltnerChannels': 1.0
        })
    )
