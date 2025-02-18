import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
