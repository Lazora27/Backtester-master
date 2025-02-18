import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
