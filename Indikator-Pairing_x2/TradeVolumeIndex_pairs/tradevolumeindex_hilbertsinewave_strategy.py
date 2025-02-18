import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
