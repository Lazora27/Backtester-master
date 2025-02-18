import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
