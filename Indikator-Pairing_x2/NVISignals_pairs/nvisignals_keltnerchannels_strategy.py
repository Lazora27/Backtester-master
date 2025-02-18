import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'KeltnerChannels': 1.0
        })
    )
