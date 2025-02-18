import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'KeltnerChannels': 1.0
        })
    )
