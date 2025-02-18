import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
